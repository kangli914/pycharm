#!/usr/bin/env node

var mysql = require('mysql')
  , tsv = require('node-tsv-json')
  , fs = require('fs')
  , ini = require('ini')


// read in db config file
var config = ini.parse( fs.readFileSync('./config.ini', 'utf-8') )

// take input args
//var environment = process.argv[2]
var cf_node = process.argv[2]
var log_files = process.argv.slice(3)

// do input validation checking


// connect to mysql database
var pool = mysql.createPool(config.database)


// loop through and parse tsv logs
for (var i in log_files){
  tsv({
    input: log_files[i],
    parseRows: true
  }, function(err, result){
    if( err )
      console.error(err)
    else{
      /*
	  // grab date of file
      var date = new Date(Date.parse(result[0][1]))
	  var rows = result.slice(1)
      */
	  
	  var imp_date = new Date()
	  
      // loop through each row of file
      for( var j in rows ){
        var cols = rows[j]
        var log = {
          cfnode: cf_node,
          impdate: imp_date
        }

        /* skip if contains # in row
        if( cols[0] == "#" )
          continue 
       
		
        // grab coloumn values
        log.test_id = cols[0]
        log.time_ms = parseInt(cols[1])
        log.details = JSON.stringify(cols.slice(2))
		*/
			
		log.dateField = 				cols[0]
		log.timeField = 				cols[1]
		log.timemsField = 			cols[2]
		log.reqStatusField  = 		cols[6]
		log.clientIPField = 			cols[9]
		log.reqHTTPType = 	  	cols[10]
		
        // build unique id
        log.log_id = log.test_id.replace(/\D+/g,'') + "" + result[0][1].replace(/\D+/g,'') + "" + String(log.time_ms)
 
        // send to database
        add_to_db(log)  
      }
    }
  })
}



function add_to_db(log){
  pool.getConnection( function(j, connection){
    connection.query('INSERT INTO logs SET ?', log, function(e,r){
      console.log(e)
      connection.release()
    }) 
  })
}

