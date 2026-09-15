.syntax unified
.thumb
.section .text.overlay_0079,"ax",%progbits
.balign 4

.global Overlay079_Init
.type Overlay079_Init,%function
.thumb_func
Overlay079_Init:
    push {r3, r4, r5, r6, lr}
    sub sp, #0xc
    ldr r6, .Lconfig_ptr
    add r3, sp, #0
    adds r4, r0, #0
    adds r2, r1, #0
    ldm r6!, {r0, r1}
    adds r5, r3, #0
    stm r3!, {r0, r1}
    ldr r0, [r6]
    str r0, [r3]
    adds r0, r2, #0
    bl sub_02189A08
    bl sub_021CF580
    ldr r2, .Lsetup_ptr
    ldr r3, .Lcallback_ptr
    adds r0, r4, #0
    adds r1, r5, #0
    bl sub_021F5260
    add sp, #0xc
    pop {r3, r4, r5, r6, pc}
.Lconfig_ptr:
    .word Overlay079_Config
.Lsetup_ptr:
    .word Overlay079_Setup
.Lcallback_ptr:
    .word callback_021F582D

.global Overlay079_Setup
.type Overlay079_Setup,%function
.thumb_func
Overlay079_Setup:
    push {lr}
    sub sp, #0x14
    movs r1, #4
    str r1, [sp]
    str r1, [sp, #4]
    ldr r1, .Lstep0_ptr
    movs r2, #0
    str r1, [sp, #0xc]
    ldr r1, .Lstep1_ptr
    str r2, [sp, #8]
    str r1, [sp, #0x10]
    add r1, sp, #0
    bl sub_021F5620
    add sp, #0x14
    pop {pc}
.Lstep0_ptr:
    .word Overlay079_Step0
.Lstep1_ptr:
    .word Overlay079_Step1

.global Overlay079_Step0
.type Overlay079_Step0,%function
.thumb_func
Overlay079_Step0:
    push {r4, r5}
    movs r4, #3
    lsls r4, r4, #12
    adds r3, r4, #0
    adds r2, r0, r4
    adds r3, #8
    adds r4, #10
    ldrh r5, [r0, r3]
    ldrh r3, [r0, r4]
    ldr r1, [r2]
    muls r3, r5, r3
    cmp r1, r3
    bge .Lstep0_return
    ldr r3, [r2, #4]
    cmp r3, #0
    bne .Lstep0_decrement
    lsls r1, r1, #6
    movs r3, #1
    adds r0, r0, r1
    str r3, [r0, #0x34]
    ldr r0, [r2]
    adds r0, r0, #1
    str r0, [r2]
    movs r0, #0
    str r0, [r2, #4]
    pop {r4, r5}
    bx lr
.Lstep0_decrement:
    subs r0, r3, #1
    str r0, [r2, #4]
.Lstep0_return:
    pop {r4, r5}
    bx lr
    .hword 0

.global Overlay079_Step1
.type Overlay079_Step1,%function
.thumb_func
Overlay079_Step1:
    push {r4, r5}
    ldr r2, [r0, #0x30]
    cmp r2, #1
    bge .Lstate1_or_done
    movs r3, #1
    ldr r4, [r0, #0x1c]
    lsls r3, r3, #12
    adds r5, r4, r3
    adds r1, r0, #0
    lsls r4, r3, #4
    adds r1, #0x1c
    str r5, [r0, #0x1c]
    cmp r5, r4
    blt .Lstep1_finish
    lsls r3, r3, #4
    subs r3, r5, r3
    str r3, [r1]
.Ladvance_state:
    adds r1, r2, #1
    str r1, [r0, #0x30]
    b .Lstep1_finish
.Lstate1_or_done:
    bne .Ldone_state
    movs r1, #1
    ldr r3, [r0, #0x1c]
    lsls r1, r1, #12
    adds r4, r3, r1
    lsls r3, r1, #3
    str r4, [r0, #0x1c]
    cmp r4, r3
    blt .Lstep1_finish
    lsls r1, r1, #3
    str r1, [r0, #0x1c]
    b .Ladvance_state
.Ldone_state:
    movs r1, #1
    str r1, [r0, #0x38]
.Lstep1_finish:
    ldr r0, [r0, #0x38]
    pop {r4, r5}
    bx lr
    .hword 0

.global Overlay079_Config
.type Overlay079_Config,%object
Overlay079_Config:
    .word 0
    .word 0
    .word 0x00108000
.global Overlay079_StaticInit
Overlay079_StaticInit:
    .word 0
