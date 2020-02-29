# Header file generator

## Installation
 - Install contents of bison-3.4
 - Run sudo apt-get install flex
 - Install contents of radare2-src/
 - Run r2pm --init
 - Run r2pm -i r2ghidra-dec

## Example
```
chase@chase:~/github/generate-headers$ ./generate.py grep grep.h
Found 14 functions
  int sym.fts_set(int placeholder_0, int arg2, int arg3)
  int sym._obstack_memory_used(int arg1)
  int sym.fts_children(int arg1, int arg2)
  int * sym._obstack_newchunk(int arg1, int arg2)
  void sym._fini()
  void sym._obstack_free(int arg1, int arg2)
  int ** sym._obstack_begin(int arg1, int arg2, int arg3, int arg4, int arg5)
  int * sym.fts_open(int arg1, int arg2, int arg3)
  int *sym.fts_read(int arg7, int placeholder_1, int placeholder_2, int placeholder_3,            int placeholder_4, int placeholder_5, int placeholder_6, int placeholder_7,            int arg1)
  int sym.fts_close(int arg1)
  void sym._init()
  int main(int argc, char **argv)
  void fcn.00005370()
  void fcn.00005370()
Writing .h file
chase@chase:~/github/generate-headers$ 
```

Results are in `grep.h`
```
chase@chase:~/github/generate-headers$ cat grep.h 
int sym.fts_set(int placeholder_0, int arg2, int arg3);
int sym._obstack_memory_used(int arg1);
int sym.fts_children(int arg1, int arg2);
int * sym._obstack_newchunk(int arg1, int arg2);
void sym._fini();
void sym._obstack_free(int arg1, int arg2);
int ** sym._obstack_begin(int arg1, int arg2, int arg3, int arg4, int arg5);
int * sym.fts_open(int arg1, int arg2, int arg3);
int *sym.fts_read(int arg7, int placeholder_1, int placeholder_2, int placeholder_3,            int placeholder_4, int placeholder_5, int placeholder_6, int placeholder_7,            int arg1);
int sym.fts_close(int arg1);
void sym._init();
int main(int argc, char **argv);
void fcn.00005370();
void fcn.00005370();
```
