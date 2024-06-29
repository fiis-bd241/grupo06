import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { DataGrid } from '@mui/x-data-grid';

const LotesTableC = () => {
    const [rows, setRows] = useState([]);

    useEffect(() => {
        axios.get('https://sistema-web-v.onrender.com/sistema/lotesC1/')
            .then(response => {
                const data = response.data.map((item, index) => ({
                    id: index + 1,
                    dia: item.dia,
                    cantidad_lotes: item.cantidad_lotes
                }));
                setRows(data);
            })
            .catch(error => {
                console.error('Error fetching data:', error);
            });
    }, []);

    const columns = [
        { field: 'dia', headerName: 'Día', width: 100 },
        { field: 'cantidad_lotes', headerName: 'Cantidad de Lotes', width: 100}
    ];

    return (
        <div style={{ height: 400, width: '50%' }}>
            <DataGrid rows={rows} columns={columns} pageSize={5} />
        </div>
    );
};

export default LotesTableC;
