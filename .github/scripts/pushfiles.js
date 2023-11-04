const fs = require('fs');
const { Octokit } = require('@octokit/rest');

const octokit = new Octokit({
    auth: {
        id: process.env.APP_ID,
        privateKey: process.env.PRIVATE_KEY,
    },
});

console.log('APP_ID', process.env.APP_ID);
console.log('PRIVATE_KEY', process.env.PRIVATE_KEY);

const owner = 'sukamat';
const repo = 'repo-b';
const filePath = 'file.txt';
const fileContent = 'Hello, GitHub Actions!';

octokit.repos.createOrUpdateFileContents({
    owner,
    repo,
    path: filePath,
    message: 'Add file via GitHub Actions',
    content: Buffer.from(fileContent).toString('base64'),
});