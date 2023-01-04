//STATUS: FAILED

function insert(y, s, m, g, c, t) {
    var table = document.getElementById("table");
    var row = table.insertRow();
    var year = row.insertCell(0);
    var sem = row.insertCell(1);
    var grade = row.insertCell(1);
    var mod = row.insertCell(1);
    var mc = row.insertCell(1);
    var type = row.insertCell(1);

    year.innerHTML = y;
    sem.innerHTML = s;
    grade.innerHTML = g;
    mod.innerHTML = m;
    mc.innerHTML = c;
    type.innerHTML = t;
}

//import './Package Datas/xlsx/xlsx.js'

XLSX = require('./Package Datas/xlsx');

// Reading our test file
const file = XLSX.readFile('D:/Javascript/practice/NUS Acad Performance.xlsx');

let data = [];
const sheets = file.SheetNames;

for (let i = 0; i < sheets.length; i++) {
    const temp = XLSX.utils.sheet_to_json(
        file.Sheets[file.SheetNames[i]]);
    temp.forEach((res) => {
        data.push(res)
    });
}

//console.log(data)
/*
for (let i = 0; i < data.length; i++) {
    insert(data[i].Year,
        data[i].Semester,
        data[i].Module,
        data[i].Grade,
        data[i].MC,
        data[i].Type);
}*/
