# Header file generator

## Installation
 - Install contents of bison-3.4
 - Run sudo apt-get install flex
 - Install contents of radare2-src/
 - Run r2pm --init
 - Run r2pm -i r2ghidra-dec

## Example
```
chase@chase:~/github/generate-headers$ ./generate.py binary binary.h 
Found 9 functions
  void sym.deregister_tm_clones()
  void sym.register_tm_clones()
  void sym.__libc_csu_fini()
  void sym._fini()
  void sym.hash(int arg1, int arg2)
  void sym.__libc_csu_init(int arg1, int arg2, int arg3)
  int main()
  void sym._init()
  void sym._init()
Writing .h file
chase@chase:~/github/generate-headers$ 
```

Results are in `binary.h`
```
chase@chase:~/github/generate-headers$ cat binary.h 
void sym.deregister_tm_clones();
void sym.register_tm_clones();
void sym.__libc_csu_fini();
void sym._fini();
void sym.hash(int arg1, int arg2);
void sym.__libc_csu_init(int arg1, int arg2, int arg3);
int main();
void sym._init();
void sym._init();
```
