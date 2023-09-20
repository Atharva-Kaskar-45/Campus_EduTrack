document.addEventListener('DOMContentLoaded', () => {
    const searchButton = document.getElementById('search-button');
    const searchInput = document.getElementById('search-input');
    const studentDetails = document.getElementById('student-details');

    searchButton.addEventListener('click', async () => {
        const searchQuery = searchInput.value.trim();

        if (searchQuery) {
            try {
                const response = await fetch(`/api/students?query=${searchQuery}`);
                if (response.ok) {
                    const data = await response.json();
                    displayStudentData(data);
                } else {
                    console.error('Failed to fetch student data');
                }
            } catch (error) {
                console.error('Error fetching student data:', error);
            }
        } else {
            studentDetails.innerHTML = '<p>Please enter a search query.</p>';
        }
    });

    function displayStudentData(data) {
        studentDetails.innerHTML = '';

        if (data.length === 0) {
            studentDetails.innerHTML = '<p>No matching students found.</p>';
            return;
        }

        data.forEach(student => {
            const studentCard = document.createElement('div');
            studentCard.classList.add('student-card');
            studentCard.innerHTML = `
                <h3>${student.name}</h3>
                <p>PRN: ${student.prn}</p>
                <p>Program: ${student.program}</p>
                <p>Batch: ${student.batch}</p>
            `;
            studentDetails.appendChild(studentCard);
        });
    }
});
