
const getAgenciesUsedByCompetitors = async () => {
    try {
        const response = await fetch("/static/config.json");
        if (!response.ok) {
            throw new Error(`Failed to fetch config.json: ${response.status} ${response.statusText}`);
        }

        const data = await response.json();

        if (data.AgenciesUsedByCompetitors) {
            return data.AgenciesUsedByCompetitors;
        } else {
            return null; // or an empty array or whatever is appropriate
        }
    } catch (error) {
        console.error("Error fetching config.json:", error);
        return null; // or handle the error appropriately
    }
};


const getVesselsOfCompetitorAgencies = async (AgenciesUsedByCompetitors) => {
    try {
        const routeParams = AgenciesUsedByCompetitors.join(',');

        const response = await fetch(`/api/get_ships?AgencyNames=${routeParams}`);
        if (!response.ok) {
            throw new Error(`Error fetching data: ${response.status} ${response.statusText}`);
        }

        const data = await response.json();

        if (data.AgencyShipMapping) {
            return data.AgencyShipMapping;
        } else {
            return {}; // Return an empty object or handle the case when data is not available
        }
    } catch (error) {
        console.error("Error:", error);
        throw error; // Rethrow the error to propagate it to the caller
    }
};


const getPortsVisitedByVessel = async (vesselName) => {
    try {
        const response = await fetch(`/api/get_ports_visited?VesselName=${encodeURIComponent(vesselName)}`);
        
        if (!response.ok) {
            throw new Error(`Failed to fetch data: ${response.status} ${response.statusText}`);
        }

        const data = await response.json();

        if (data.error) {
            throw new Error(data.error);
        }

        const portsVisited = data.PortsVisited;

        // Map the data into the desired format
        const result = portsVisited.map(port => ({
            PortName: port['Port Name'],
            ProductType: port['Product Type'],
            Quantity: port.Quantity,
            FOBPricePerUnitAUD: port['FOB Price per Unit in AUD'],
        }));

        return result;
    } catch (error) {
        console.error(`Error getting ports visited: ${error}`);
        return [];
    }
}

const collateData = async () => {
    // a map of with the key being the agency name and the value being the an object with information including the product imported by them, the date of arrival, total volume, and FOB price per unit in AUD.
    let agencies = await getAgenciesUsedByCompetitors()
    let agencyVesselMap = {}
    agencies.forEach(async (agency) => {
        let vessels = await getVesselsOfCompetitorAgencies([agency])
        agencyVesselMap[agency] = vessels
    })
    return agencyVesselMap
    // let map = new Map()
    // const vessels = await getVesselsOfCompetitorAgencies()
    // console.log(vessels)
}
collateData().then((data) => {
    let table = document.getElementById("collated-data");
    console.log(data);
});



let jsonData;
fetch('get_dash_data')
    .then(response => response.json())
    .then(data => {
        // Get the tbody element by ID
        const tbody = document.getElementById('collated-data');
        // data = JSON.parse(data);
        console.log(data);
        jsonData = data;
        // Loop through the data and create table rows
        jsonData.forEach(item => {
            const row = document.createElement('tr');
            // Loop through the keys (headings) in each item
            for (const key in item) {
                if (item.hasOwnProperty(key)) {
                    const cell = document.createElement('td');
                    cell.textContent = item[key];
                    row.appendChild(cell);
                }
            }
            let id = item['ID'];
            // Add a data-href attribute to specify the target page URL
            // row.setAttribute('data-href', '/analyse/lookup.html'); // Replace 'page2.html' with the actual URL
            row.setAttribute('data-href', `/analyse/lookup/${id}`); // Replace 'page2.html' with the actual URL
            // Add a click event listener to redirect when a row is clicked
            row.addEventListener('click', () => {
                const targetUrl = row.getAttribute('data-href');
                console.log('Target URL:', targetUrl);
                if (targetUrl) {
                    window.location.href = targetUrl;
                }
            });
            // Append the row to the tbody
            tbody.appendChild(row);
  
     
        });
        company_filter();

    })
    .catch(error => {
        console.error('Error:', error);
    });





    function company_filter() {
        // Get the HTML elements
        const companyFilter = document.getElementById('company-filter');
        const tbody = document.getElementById('collated-data');
    
        // Define a function to create a dropdown option
        function createOption(value, text) {
            const option = document.createElement('option');
            option.value = value;
            option.textContent = text;
            return option;
        }
    
        // Function to populate the company name dropdown
        function populateCompanyDropdown() {
            // Get unique company names from the data
            const uniqueCompanyNames = [...new Set(jsonData.map(item => item["COMPANY NAME"]))];
    
            // Clear existing options and add a "Reset" option
            companyFilter.innerHTML = '';
            companyFilter.appendChild(createOption('All', 'All'));
    
            // Add unique company names to the dropdown
            uniqueCompanyNames.forEach(companyName => {
                companyFilter.appendChild(createOption(companyName, companyName));
            });
        }
    
        // Function to filter and populate the table
        function filterTable() {
            const selectedCompany = companyFilter.value;
    
            // Get all rows in the table
            const rows = tbody.querySelectorAll('tr');
    
            // Hide all rows initially
            rows.forEach(row => {
                row.style.display = 'none';
            });
    
            // Show rows that match the selected company or show all rows if 'All' is selected
            rows.forEach(row => {
                const companyName = row.querySelector('td:nth-child(2)').textContent; // Assuming the second column contains the company name
                if (selectedCompany === 'All' || companyName === selectedCompany) {
                    row.style.display = 'table-row';
                }
            });
        }
    
        // Add event listeners
        companyFilter.addEventListener('change', filterTable);
    
        // Initial setup
        populateCompanyDropdown(); // Call this function to populate the dropdown initially
        filterTable();
    }
    
    // Call the company_filter function when the page loads
    document.addEventListener('DOMContentLoaded', company_filter);
    