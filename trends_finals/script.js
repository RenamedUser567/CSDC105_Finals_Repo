const searchBox = document.getElementById('search-box');
const filterLocation = document.getElementById('filter-location');
const filterCourse = document.getElementById('filter-course');
const universityList = document.getElementById('university-list');

// Replace with your actual university data
const universities = [
  { name: 'University A', location: 'State 1', course: 'Engineering' },
  { name: 'University B', location: 'State 2', course: 'Computer Science' },
  // Add more universities
];

function updateList() {
  const searchTerm = searchBox.value.toLowerCase();
  const selectedLocation = filterLocation.value;
  const selectedCourse = filterCourse.value;

  universityList.innerHTML = ''; // Clear previous results

  universities.forEach(university => {
    const universityName = university.name.toLowerCase();
    const shouldInclude =
      (searchTerm === '' || universityName.includes(searchTerm)) &&
      (selectedLocation === 'all' || university.location === selectedLocation) &&
      (selectedCourse === 'all' || university.course === selectedCourse);

    if (shouldInclude) {
      const listItem = document.createElement('li');
      listItem.textContent = university.name;
      universityList.appendChild(listItem);
    }
  });
}

searchBox.addEventListener('keyup', updateList);
filterLocation.addEventListener('change', updateList);
filterCourse.addEventListener('change', updateList);

// Call updateList initially to display all universities on page load
updateList();
