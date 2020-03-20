

const readXlsxFile = require('read-excel-file/node');
readXlsxFile('Desktop/Olawale/projects/analyzeExcel/Workers.xlsx').then((rows) => {
   rows.forEach((col)=>{
       col.forEach((data)=>{
           console.log(data);
       })
   })
   
})

