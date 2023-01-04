function is_number(word) {
    var regex = /^[a-zA-Z]+$/;
    if (word.match(regex)) {
        alert(word + ' is not a valid number.');
        return false;
    } else {
        return true;
    }
}

function is_grade(word) {
    if (word.length == 1) {
        if (word.match(/^[A-D]$/) || word === 'F') {
            return true;
        }
    } else if (word.length == 2) {
        if (word.match(/^[A-B][+-]$/) || word.match(/^[C-D][+]$/)) {
            return true;
        }
    }

    alert('Invalid grade. Make sure that it is capitalised.');
    return false;
}
