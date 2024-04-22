const express = require('express');
const bodyParser = require('body-parser');
const jwt = require('jsonwebtoken');
const bcrypt = require('bcryptjs');

const app = express();
app.use(bodyParser.json());

let users = [];

app.post('/register', (req, res) => {
    const hashedPassword = bcrypt.hashSync(req.body.password, 8);
    users.push({
        id: users.length + 1,
        username: req.body.username,
        password: hashedPassword
    });
    res.status(200).send({ message: 'User registered successfully!' });
});

app.post('/login', (req, res) => {
    const user = users.find(user => user.username === req.body.username);
    if (!user) return res.status(404).send('No user found.');
    const passwordIsValid = bcrypt.compareSync(req.body.password, user.password);
    if (!passwordIsValid) return res.status(401).send({ auth: false, token: null });
    const token = jwt.sign({ id: user.id }, 'supersecret', {
        expiresIn: 86400 // expires in 24 hours
    });
    res.status(200).send({ auth: true, token: token });
});

app.get('/me', (req, res) => {
    const token = req.headers['x-access-token'];
    if (!token) return res.status(401).send({ auth: false, message: 'No token provided.' });
    jwt.verify(token, 'supersecret', (err, decoded) => {
        if (err) return res.status(500).send({ auth: false, message: 'Failed to authenticate token.' });
        res.status(200).send(users[decoded.id - 1]);
    });
});

app.listen(3000, () => {
    console.log('Server is running on port 3000');
});