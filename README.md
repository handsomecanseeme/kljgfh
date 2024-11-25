```python
   _____                       _______                      
 /      \                     /       \                     
/$$$$$$  | __    __   _______ $$$$$$$  |  ______   __    __ 
$$ |__$$ |/  |  /  | /       |$$ |__$$ | /      \ /  \  /  |            
$$    $$ |$$ |  $$ |/$$$$$$$/ $$    $$/ /$$$$$$  |$$  \/$$/ 
$$$$$$$$ |$$ |  $$ |$$      \ $$$$$$$/  $$    $$ | $$  $$<  
$$ |  $$ |$$ \__$$ | $$$$$$  |$$ |      $$$$$$$$/  /$$$$  \ 
$$ |  $$ |$$    $$/ /     $$/ $$ |      $$       |/$$/ $$  |
$$/   $$/  $$$$$$/  $$$$$$$/  $$/        $$$$$$$/ $$/   $$/

    /\_____/\
   /  o   o  \
  ( ==  ^  == )
   )         (
  (           )
 ( (  )   (  ) ) 
(__(__)___(__)__)

```


# Auspex Tools Quickstart Guide

## Introduction

Auspex Tools is a set of utilities designed to analyze and detect inconsistencies in Ethereum transaction fee mechanisms (TFM). The tool leverages fuzzing techniques to identify potential issues in smart contracts and the Ethereum blockchain.

## Prerequisites

```shell
                      (`.-,')
                    .-'     ;
                _.-'   , `,-
          _ _.-'     .'  /._
        .' `  _.-.  /  ,'._;)
       (       .  )-| (
        )`,_ ,'_,'  \_;)
('_  _,'.'  (___,))
 `-:;.-'
```

Before you start, ensure you have the following dependencies installed:

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

```shell

 /\     /\
{  `---'  }
{  O   O  }
~~>  V  <~~
 \  \|/  /
  `-----'____
  /     \    \_
 {       }\  )_\_   _
 |  \_/  |/ /  \_\_/ )
  \__/  /(_/     \__/
    (__/
```

1. **Navigate to the Auspex Tools Directory:**
   ```sh
   cd ./Auspex_tools/cmd/auspex
   ```

2. **Build the Fuzzing Target**
   ```sh
go-fuzz-build
   ```

3.Running the Tool

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

1.**Start the Fuzzing Process**
   ```sh
go-fuzz -bin=auspex-fuzz.zip -workdir=workdir
   ```
