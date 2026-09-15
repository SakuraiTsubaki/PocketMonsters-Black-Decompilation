.syntax unified
.thumb
.section .text.overlay_0062,"ax",%progbits
.balign 4

.global Overlay062_Function0
.type Overlay062_Function0,%function
.thumb_func
Overlay062_Function0:
    push {r3, r4, r5, r6, r7, lr}
    adds r4, r0, #0
    bl sub_02188C80
    bl sub_020120F4
    bl sub_02012EC4
    movs r1, #0x34
    bl sub_0200B3A4
    adds r5, r0, #0
    adds r0, r4, #0
    bl sub_02188D2C
    ldr r1, .Lptr_A8
    adds r4, r0, #0
    movs r2, #0
    movs r7, #0
    bl sub_021BE760
    adds r0, r4, #0
    movs r1, #0
    movs r2, #0
    bl sub_021BE480
    ldr r3, .Lptr_D0
    adds r2, r0, #0
    ldm r3!, {r0, r1}
    stm r2!, {r0, r1}
    ldr r0, [r3]
    movs r1, #0
    str r0, [r2]
    adds r0, r4, #0
    movs r2, #0
    movs r6, #1
    movs r3, #1
    bl sub_021BE4A4
    str r6, [sp]
    adds r0, r4, #0
    movs r1, #0
    movs r2, #0
    movs r3, #0
    bl sub_021BE700
    ldr r0, [r5]
    cmp r0, #0
    beq .Lreturn0
    adds r0, r4, #0
    adds r1, r7, #0
    adds r2, r7, #0
    adds r3, r6, #0
    bl sub_021BE4B4
.Lreturn0:
    pop {r3, r4, r5, r6, r7, pc}
.Lptr_A8:
    .word Overlay062_DataA8
.Lptr_D0:
    .word Overlay062_DataD0

.global Overlay062_Function1
.type Overlay062_Function1,%function
.thumb_func
Overlay062_Function1:
    push {r3, lr}
    bl sub_02188D2C
    movs r1, #0
    bl sub_021BE418
    pop {r3, pc}
    .hword 0

.global Overlay062_Function2
.type Overlay062_Function2,%function
.thumb_func
Overlay062_Function2:
    push {r3, lr}
    bl sub_02188D2C
    bl sub_021BE580
    pop {r3, pc}

.global Overlay062_Data94
Overlay062_Data94:
    .word 1
.global Overlay062_Data98
Overlay062_Data98:
    .word 0
    .word 0
    .word Overlay062_Data94
    .word 1
.global Overlay062_DataA8
Overlay062_DataA8:
    .word Overlay062_DataB8
    .word 2
    .word Overlay062_Data98
    .word 1
.global Overlay062_DataB8
Overlay062_DataB8:
    .word 0x000000D9
    .word 0
    .word 0
    .word 0x000000D9
    .word 1
    .word 0
.global Overlay062_DataD0
Overlay062_DataD0:
    .word 0x01428000
    .word 0x00008000
    .word 0x02FF8000

.global Overlay062_StaticInit
Overlay062_StaticInit:
    .word 0
