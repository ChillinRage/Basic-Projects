function get_data() {
    const url = 'https://raw.githubusercontent.com/ChillinRage/Basic-Projects/main/Academic%20Website%201/NUS%20Acad%20results.csv';
    const response = await fetch(url);       // fetch data
    const raw_data = await response.text();  // process data
    const rows     = raw_data.split('\r\n'); // split into rows
    
    return rows;
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

function update_cap() {
    const data = get_data();
    const len  = data.length;
    let total_mc = 0;
    let points   = 0;
    
    for (let i = 1; i < len; i++) {
        const row = data[i].split(',');
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
    const data   = get_data();
    const header = data[0].split(',');
    const len    = data.length;

    for (let i = 1; i < len; i++) {
        let row = data[i].split(',');
        add_row(row);
    }
    
    update_cap();
}

display();

