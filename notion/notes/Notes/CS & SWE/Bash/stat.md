# stat

- !(stat -t /usr/local/lib/*/dist-packages/google/colab > /dev/null 2>&1) && exit
    
    ```bash
    !(stat -t /usr/local/lib/*/dist-packages/google/colab > /dev/null 2>&1) && exit
    ```
    
    stat -t : Check status of file path (-t displays output in tab format)
    
    The **`> /dev/null 2>&1`** portion of a command is used to redirect the output of a command to the null device, which discards the output and prevents it from being displayed on the screen or captured in a file. The **`2>&1`** redirects standard error (stderr) to the same location as standard output (stdout). So both types of output will be discarded by the null device.
    
     && exit : if prev command executes with success status (file dir exists), then exit this shell session
    
    [Bash](../Bash%202a08c45ec15548dc968f872461395b68.md)