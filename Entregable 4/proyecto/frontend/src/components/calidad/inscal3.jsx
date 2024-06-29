// TuComponente.jsx (ejemplo básico de React)
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { DataGrid } from '@mui/x-data-grid';

const TuComponente = () => {
    const [data, setData] = useState([]);

    useEffect(() => {
        fetchData();
    }, []);

    const fetchData = async () => {
        try {
            const response = await axios.get('https://sistema-web-v.onrender.com/sistema/tu-endpoint/');
            setData(response.data);
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    };

    const columns = [
        { field: 'ID_ORDEN_PRODUCCIÓN', headerName: 'ID Orden Producción', width: 200 },
        // Define más columnas según los campos que necesites mostrar
    ];

    return (
        <div style={{ height: 400, width: '100%' }}>
            <DataGrid rows={data} columns={columns} pageSize={5} />
        </div>
    );
};

export default TuComponente;
