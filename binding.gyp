{
  "targets": [
    {
      "target_name": "helloWorld",
      "sources": [ "helloWorld.cpp" ],
      "include_dirs": [ "<!(node -e \"require('nan')\")" ]
    }
  ]
}