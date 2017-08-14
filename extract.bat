mkdir rom
ndstool.exe -x rom-base.nds -9 rom/arm9.bin -7 rom/arm7.bin -y9 rom/y9.bin -y7 rom/y7.bin -d rom/data -y rom/overlay -t rom/banner.bin -h rom/header.bin
ppmd_statsutil.exe -e -scripts -romroot "rom" "export"