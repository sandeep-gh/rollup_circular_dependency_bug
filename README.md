# To reproduce the bug
run `setup.sh` on machine with latest Python3 installed (3.8 or above)




# Rollup bug 
```
rollup v2.70.1
bundles src/main.js → dist/bundle.js...
(!) Circular dependency
src/transcrypted/addict.js -> src/transcrypted/addict.js
[!] RangeError: Maximum call stack size exceeded
RangeError: Maximum call stack size exceeded
    at Function.[Symbol.hasInstance] (<anonymous>)
    at Module.traceVariable (/home/kabira/Development/rollup_circular_dependency_bug/node_modules/rollup/dist/shared/rollup.js:12828:29)
    at Module.getVariableForExportName (/home/kabira/Development/rollup_circular_dependency_bug/node_modules/rollup/dist/shared/rollup.js:12645:35)
    at Module.traceVariable (/home/kabira/Development/rollup_circular_dependency_bug/node_modules/rollup/dist/shared/rollup.js:12831:47)
    at Module.getVariableForExportName (/home/kabira/Development/rollup_circular_dependency_bug/node_modules/rollup/dist/shared/rollup.js:12645:35)
    at Module.traceVariable (/home/kabira/Development/rollup_circular_dependency_bug/node_modules/rollup/dist/shared/rollup.js:12831:47)
    at Module.getVariableForExportName (/home/kabira/Development/rollup_circular_dependency_bug/node_modules/rollup/dist/shared/rollup.js:12645:35)
    at Module.traceVariable (/home/kabira/Development/rollup_circular_dependency_bug/node_modules/rollup/dist/shared/rollup.js:12831:47)
    at Module.getVariableForExportName (/home/kabira/Development/rollup_circular_dependency_bug/node_modules/rollup/dist/shared/rollup.js:12645:35)
    at Module.traceVariable (/home/kabira/Development/rollup_circular_dependency_bug/node_modules/rollup/dist/shared/rollup.js:12831:47)
```

