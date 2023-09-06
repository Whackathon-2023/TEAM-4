
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