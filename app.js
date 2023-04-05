const express = require('express');
const bodyParser = require('body-parser');
const { spawn } = require('child_process');

const app = express();

app.get('/style.css', function(req, res) {
	res.type('text/css');
	res.sendFile(__dirname + '/style.css');
  });

  
app.use(bodyParser.urlencoded({ extended: true }));

/*
app.use(function (req, res, next) {

    // Website you wish to allow to connect
    res.setHeader('Access-Control-Allow-Origin', 'http://127.0.0.1:3000');

    // Request methods you wish to allow
    res.setHeader('Access-Control-Allow-Methods', 'POST');


    // Set to true if you need the website to include cookies in the requests sent
    // to the API (e.g. in case you use sessions)
    res.setHeader('Access-Control-Allow-Credentials', true);

    // Pass to next layer of middleware
    next();
});*/

// Routes
app.get('/', (req, res) => {
	res.sendFile(__dirname + '/index.html');
});



//-----------------------------------------------------------------------------------------//
//Taux de consultation des patients en France sur une période de temps Y
//-----------------------------------------------------------------------------------------//
app.post('/TotalConsultPeriode', (req, res) => {
  const param1 = req.body.param1;
  const param2 = req.body.param2;

  // Validation des paramètres
 
  const python = spawn('python', ['./scripts/TotalConsultPeriode.py',param1,param2]);


  python.stdout.on('data', (data) => {
    console.log(`stdout: ${data}`);
    res.send(data);
  });

  python.stderr.on('data', (data) => {
    console.error(`stderr: ${data}`);
    res.status(500).send(`Erreur: ${data}`);
  });

  python.on('close', (code) => {
    console.log(`Le script Python a quitté avec le code ${code}`);
  });
});


//-----------------------------------------------------------------------------------------//
//Taux de consultation des patients par rapport à un diagnostic X sur une période de temps Y
//-----------------------------------------------------------------------------------------//
app.post('/TotalConsultDiagPeriode', (req, res) => {
	const diag1 = req.body.diag1;
  
	// Validation des paramètres
   
	const python = spawn('python', ['./scripts/TotalConsultDiagPeriode.py',diag1]);
  
  
	python.stdout.on('data', (data) => {
	  console.log(`stdout: ${data}`);
	  res.send(data);
	});
  
	python.stderr.on('data', (data) => {
	  console.error(`stderr: ${data}`);
	  res.status(500).send(`Erreur: ${data}`);
	});
  
	python.on('close', (code) => {
	  console.log(`Le script Python a quitté avec le code ${code}`);
	});
  });

//-----------------------------------------------------------------------------------------//
//Taux de consultation par professionnel
//-----------------------------------------------------------------------------------------//
app.post('/TotalConsultParProfessionnel', (req, res) => {
  
	// Validation des paramètres
   
	const python = spawn('python', ['./scripts/TotalConsultParProfessionnel.py']);
  
  
	python.stdout.on('data', (data) => {
	  console.log(`stdout: ${data}`);
	  res.send(data);
	});
  
	python.stderr.on('data', (data) => {
	  console.error(`stderr: ${data}`);
	  res.status(500).send(`Erreur: ${data}`);
	});
  
	python.on('close', (code) => {
	  console.log(`Le script Python a quitté avec le code ${code}`);
	});
  });


//-----------------------------------------------------------------------------------------//
//PORT DU SERVEUR NODE 
//-----------------------------------------------------------------------------------------//
app.listen(3000, () => {
  console.log('Le serveur est en cours d\'exécution sur le port 3000');
});

