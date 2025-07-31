const dropZone = document.getElementById('drop-zone');
const fileInput = document.getElementById('file-input');
const progressContainer = document.getElementById('progress-container');
const resultContainer = document.getElementById('result-container');

dropZone.addEventListener('click', () => fileInput.click());

dropZone.addEventListener('dragover', (e) => {
    e.preventDefault();
    dropZone.classList.add('dragover');
});

dropZone.addEventListener('dragleave', () => {
    dropZone.classList.remove('dragover');
});

dropZone.addEventListener('drop', (e) => {
    e.preventDefault();
    dropZone.classList.remove('dragover');
    const files = e.dataTransfer.files;
    if (files.length) {
        handleFiles(files);
    }
});

fileInput.addEventListener('change', () => {
    if (fileInput.files.length) {
        handleFiles(fileInput.files);
    }
});

function handleFiles(files) {
    const formData = new FormData();
    for (const file of files) {
        formData.append('files[]', file);
    }

    progressContainer.innerHTML = '<p>Uploading...</p>';

    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        progressContainer.innerHTML = '';
        displayResults(data);
    })
    .catch(error => {
        progressContainer.innerHTML = `<p>Error: ${error.message}</p>`;
    });
}

function displayResults(data) {
    resultContainer.innerHTML = '<h2>Processed Files</h2>';

    if (data.processed_files && data.processed_files.length > 0) {
        const ul = document.createElement('ul');
        data.processed_files.forEach(file => {
            const li = document.createElement('li');
            li.className = 'file-item';
            li.innerHTML = `
                ${file.original_name}
                <a href="/download/file/${file.original_name}" class="download-link">Download</a>
                <p>Removed: ${file.report.metadata_removed.join(', ')}</p>
            `;
            ul.appendChild(li);
        });
        resultContainer.appendChild(ul);
        if (data.processed_files.length > 1) {
            resultContainer.innerHTML += '<a href="/download/zip" class="download-link">Download all as ZIP</a>';
        }
    }

    if (data.errors && data.errors.length > 0) {
        const errorsUl = document.createElement('ul');
        data.errors.forEach(err => {
            const li = document.createElement('li');
            li.className = 'file-item error';
            li.innerHTML = `${err.filename}: ${err.error}`;
            errorsUl.appendChild(li);
        });
        resultContainer.appendChild(errorsUl);
    }
}
