```python
  _____                       _______                                       /\_____/\
/      \                     /       \                                     /  o   o  \
/$$$$$$  | __    __   _______ $$$$$$$  |  ______   __    __               ( ==  ^  == )
$$ |__$$ |/  |  /  | /       |$$ |__$$ | /      \ /  \  /  |               )         (
$$    $$ |$$ |  $$ |/$$$$$$$/ $$    $$/ /$$$$$$  |$$  \/$$/               (           )
$$$$$$$$ |$$ |  $$ |$$      \ $$$$$$$/  $$    $$ | $$  $$<               ( (  )   (  ) ) 
$$ |  $$ |$$ \__$$ | $$$$$$  |$$ |      $$$$$$$$/  /$$$$  \             (__(__)___(__)__)
$$ |  $$ |$$    $$/ /     $$/ $$ |      $$       |/$$/ $$  |                     \\
$$/   $$/  $$$$$$/  $$$$$$$/  $$/        $$$$$$$/ $$/   $$/                       \\=======//
```


# Auspex Tools Quickstart Guide

## Prerequisites

Before you start, ensure you have the following dependencies installed:

- Ubuntu xxx LTS
- Golang
- Go-Ethereum
- Go-Fuzz

You can use the following instructions to configure corresponding dependencies.

1. **Golang Runtime:**
   - Download and install the latest version of Go from the official website: [https://go.dev/dl/](https://go.dev/dl/)
   - Follow the installation instructions provided on the site.

2. **Go-Ethereum Environment:**
   - Clone the go-ethereum repository:
     ```sh
     git clone https://github.com/ethereum/go-ethereum.git
     cd go-ethereum
     make geth
     ```
   - Ensure `geth` is added to your PATH.

3. **Go-Fuzz Environment:**
   - Install go-fuzz:
     ```sh
     go install -v github.com/dvyukov/go-fuzz/go-fuzz@latest
     go install -v github.com/dvyukov/go-fuzz/go-fuzz-build@latest
     ```
   - Add the `go-fuzz` and `go-fuzz-build` binaries to your PATH.

## Setup Instructions

1. **Navigate to the Auspex Tools Directory:**
   ```sh
   cd ./Auspex_tools/cmd/auspex
   ```

2. **Build the Fuzzing Target**
   ```sh
   go-fuzz-build
   ```

3. **Running the Tool**
   ```shell
   go-fuzz -bin=auspex-test -workdir=workdir
   ```
   ```shell
          _                        
          \`*-.                    
           )  _`-.                 
          .  : `. .                
          : _   '  \               
          ; *` _.   `*-._          
          `-.-'          `-.       
            ;       `       `.     
            :.       .        \    
            . \  .   :   .-'   .   
            '  `+.;  ;  '      :   
            :  '  |    ;       ;-. 
            ; '   : :`-:     _.`* ;
   [bug] .*' /  .*' ; .*`- +'  `*' 
         `*-*   `*-*  `*-*'
   ```
