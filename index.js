var bindings = require('bindings');
var helloWorld = bindings('helloWorld');

helloWorld.print(process.argv[2]);
