ENTRY(Overlay079_Init)
sub_02189A08 = 0x02189A08;
sub_021CF580 = 0x021CF580;
sub_021F5260 = 0x021F5260;
sub_021F5620 = 0x021F5620;
callback_021F582D = 0x021F582D;
SECTIONS
{
  . = 0x021F5A80;
  .text : { *(.text.overlay_0079) }
  /DISCARD/ : { *(.ARM.attributes) *(.comment) *(.note*) }
}
