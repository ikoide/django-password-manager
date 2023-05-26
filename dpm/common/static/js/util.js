// Copy function used in copying password to clipboard
function copy(text) {
    navigator.clipboard.writeText(text);
}

// Function to generate random string password for generator
function gen_pass(length) {
    let result = '';
    const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!#$%&()*+-/:;<=>?@[\]^_`{|}~';
    const charactersLength = characters.length;
    let counter = 0;
    while (counter < length) {
        result += characters.charAt(Math.floor(Math.random() * charactersLength));
        counter += 1;
    }

    let pass = document.getElementById("generated-password");
    pass.value = result;
}

