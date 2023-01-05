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

async function display() {
    const url = 'https://raw.githubusercontent.com/ChillinRage/Basic-Projects/main/Academic%20Website%201/NUS%20Acad%20results.csv';
    const response = await fetch(url);       // fetch data
    const raw_data = await response.text();  // process data
    const rows     = raw_data.split('\r\n'); // split into rows
    const header   = rows[0].split(',');
    const len      = rows.length;

    for (let i = 1; i < len; i++) {
        let row = rows[i].split(',');
        add_row(row);
    }
}

display();
