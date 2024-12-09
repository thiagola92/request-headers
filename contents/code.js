console.log("Hello from code.js")

async function print_file() {
    let resp = await fetch("file.json")
    
    if (resp.ok) {
        console.log(await resp.json())
    } else {
        console.log("Failed to print file")
    }
}

print_file()