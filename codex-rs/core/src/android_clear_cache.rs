use core::arch::asm;
use std::ffi::c_void;

#[unsafe(no_mangle)]
pub unsafe extern "C" fn __clear_cache(begin: *mut c_void, end: *mut c_void) {
    let start = begin as usize;
    let finish = end as usize;
    if start >= finish {
        return;
    }

    let mut cache_type_register: usize;
    unsafe {
        asm!(
            "mrs {ctr}, ctr_el0",
            ctr = out(reg) cache_type_register,
            options(nomem, nostack, preserves_flags),
        );
    }

    let dcache_line_size = 4usize << ((cache_type_register >> 16) & 0xF);
    let icache_line_size = 4usize << (cache_type_register & 0xF);

    let mut dcache_line = start & !(dcache_line_size - 1);
    while dcache_line < finish {
        unsafe {
            asm!(
                "dc civac, {line}",
                line = in(reg) dcache_line,
                options(nostack),
            );
        }
        dcache_line += dcache_line_size;
    }

    unsafe {
        asm!("dsb ish", options(nostack));
    }

    let mut icache_line = start & !(icache_line_size - 1);
    while icache_line < finish {
        unsafe {
            asm!(
                "ic ivau, {line}",
                line = in(reg) icache_line,
                options(nostack),
            );
        }
        icache_line += icache_line_size;
    }

    unsafe {
        asm!("dsb ish", "isb", options(nostack));
    }
}
