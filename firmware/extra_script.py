Import("env")
import os
import sys

def after_build(source, target, env):
    firmware_path = str(target[0])

    print(f"\n\n=== Uploading {firmware_path} using Arduino dfu-util ===\n")

    dfu_util = "/Users/owhite/Library/Arduino15/packages/arduino/tools/dfu-util/0.11.0-arduino5/dfu-util"

    cmd = (
        f'"{dfu_util}" '
        '--device 0x2341:0x0070 '
        f'-D "{firmware_path}" -Q'
    )

    print(f"Running: {cmd}\n")

    exit_code = os.system(cmd)

    if exit_code != 0:
        print(f"❌ Upload failed with exit code {exit_code}")
        sys.exit(exit_code)
    else:
        print("✅ Upload complete!")

env.AddPostAction("$BUILD_DIR/${PROGNAME}.bin", after_build)
