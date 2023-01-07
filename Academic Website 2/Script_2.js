
function is_number(word) {
    var regex = /^[a-zA-Z]+$/;
    if (isempty(word)) {
        return false;
    } else if (word.match(regex)) {
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

    alert('Invalid grade. Ensure that it is capitalised.');
    return false;
}

function is_module(word) {
    if (isempty(word)) {
        return false;
    } else {
        const valid = (word === word.toUpperCase());
        if (!valid) {
            alert('Ensure the module code is in capital letters.');
        }

        return valid
    }

}

function get_data() {
    const storage = window.localStorage;
    const len = storage.length + 1;  // 1-indexed
    const data = [];

    for (let i = 1; i < len; i++) {
        var temp = storage.getItem(i.toString());
        data.push(JSON.parse(temp));
    }

    return data;
}

function insert_row(data) {
    var table  = document.getElementById("table");
    var row    = table.insertRow();
    var year   = row.insertCell(0);
    var sem    = row.insertCell(1);
    var mod    = row.insertCell(2);
    var grade  = row.insertCell(3);
    var mc     = row.insertCell(4);
    var remark = row.insertCell(5);

    year.innerHTML   = data[0];
    sem.innerHTML    = data[1];
    mod.innerHTML    = data[2];
    grade.innerHTML  = data[3];
    mc.innerHTML     = data[4];
    remark.innerHTML = data[5];
}

function isempty(word) {
    if (word === '') {
        alert('Error. There is an empty field.');
    }

    return word === '';
}

function add_row() {
    var year  = document.querySelector('#year').value.trim();
    var sem   = document.querySelector('#semester').value.trim();
    var mod   = document.querySelector('#module').value.trim();
    var grade = document.querySelector('#grade').value.trim();
    var mc    = document.querySelector('#mc').value.trim();
    var type  = document.querySelector('#type').value.trim();

    if (is_number(year) && is_number(sem) && is_module(mod) && is_grade(grade) && is_number(mc) && !isempty(type)) {
        const arr = [year, sem, mod, grade, mc, type];
        insert_row(arr);
        add_to_storage(arr);

        document.getElementById('year').value     = '';
        document.getElementById('semester').value = '';
        document.getElementById('module').value   = '';
        document.getElementById('grade').value    = '';
        document.getElementById('mc').value       = '';
        document.getElementById('type').value     = '';

        update_cap();
    }
}

function add_to_storage(details) {
    const key = window.localStorage.length + 1;
    window.localStorage.setItem(key, JSON.stringify(details));
}

function delete_row() {
    const mod = prompt('Enter Module code to delete').trim();
    if (mod === '') {
        alert('Invalid/Empty input');
    } else {
        const index = delete_from_storage(mod); //delete and get row of module
        if (index === -1) {
            alert(mod + ' is not found.');
        } else {
            var table = document.getElementById("table");
            table.deleteRow(index + 1);
            alert(mod + ' has been removed.');
        }
    }
    update_cap();
}

function delete_from_storage(mod) {
    const storage = window.localStorage;

    for (let i = 1; i < storage.length + 1; i++) {
        var temp = JSON.parse(storage.getItem(i));
        if (temp[2] === mod) {
            storage.removeItem(i);
            console.log(temp);
            return i - 1;
        }
    }

    return -1;
}

async function update_cap() {
    const data = await get_data();
    let total_mc = 0;
    let points = 0;

    for (const row of data) {
        total_mc += JSON.parse(row[4]);
        switch (row[3]) {
            case 'A+':
                points += (5 * JSON.parse(row[4]));
                break;
            case 'A':
                points += (5 * JSON.parse(row[4]));
                break;
            case 'A-':
                points += (4.5 * JSON.parse(row[4]));
                break;
            case 'B+':
                points += (4 * JSON.parse(row[4]));
                break;
            case 'B':
                points += (3.5 * JSON.parse(row[4]));
                break;
            case 'B-':
                points += (3 * JSON.parse(row[4]));
                break;
            case 'C+':
                points += (2.5 * JSON.parse(row[4]));
                break;
            case 'C':
                points += (2 * JSON.parse(row[4]));
                break;
            case 'D+':
                points += (1.5 * JSON.parse(row[4]));
                break;
            case 'D':
                points += (1 * JSON.parse(row[4]));
                break;
            case 'F':
                points += (0 * JSON.parse(row[4]));
                break;
        }
    }

    if (total_mc > 0) {
        document.getElementById('cap_label').innerHTML = (points / total_mc).toFixed(2);
    }
}

async function display() {
    const data = await get_data();

    for (const row of data) {
        insert_row(row);
    }

    update_cap();
}


function main() {
    window.add_row = add_row;
    window.delete_row = delete_row;
    display();
}

main();
