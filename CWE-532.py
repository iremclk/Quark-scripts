import globVariable
from quark.script import findMethodInAPK

input = globVariable.applicationName
SAMPLE_PATH = input
TARGET_METHOD = [
    "Landroid/util/Log;",                       # class name
    "d",                                        # method name
    "(Ljava/lang/String; Ljava/lang/String;)I"  # descriptor
]
CREDENTIAL_KEYWORDS = [
    "token",
    "decrypt",
    "password"
]

methodsFound = findMethodInAPK(SAMPLE_PATH, TARGET_METHOD)

for debugLogger in methodsFound:
    arguments = debugLogger.getArguments()

    for keyword in CREDENTIAL_KEYWORDS:
        if keyword in arguments[1]:
            print(f"CWE-532 is detected in method, {debugLogger.fullName}")
