# Use the built-in `platform` module to print out the following info:
import platform
placeholder = " "
Platform = platform.platform()
Compiler = platform.python_compiler()
Python = platform.python_version()
System = platform.system()
Release = platform.release()
Processor = platform.processor()
print(f"{'Platform:':>10} {Platform}",)  # 
print(f"{'Compiler:':>10} {Compiler}",)  # 
print(f"{'Python:':>10} {Python}",)  # 
print(f"{'System:':>10} {System}",)  # 
print(f"{'Release:':>10} {Release}",)  # 
print(f"{'Processor:':>10} {Processor}",)  # 