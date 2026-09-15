ENTRY(Overlay074_GetRecord)
SECTIONS
{
  . = 0x021F54E0;
  .text : { *(.text.overlay_0074) }
  /DISCARD/ : { *(.ARM.attributes) *(.comment) *(.note*) }
}
