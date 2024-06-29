import React, { useEffect, useState } from 'react';
import { DataGrid } from '@mui/x-data-grid';
import { Button, MenuItem, Select, FormControl, InputLabel } from '@mui/material';
import axios from 'axios';

const LotesAlmacen = () => {
    const [rows, setRows] = useState([]);
    const [proveedores, setProveedores] = useState([]);
    const [materiasPrimas, setMateriasPrimas] = useState([]);
    const [selectedProveedor, setSelectedProveedor] = useState('');
    const [selectedMateriaPrima, setSelectedMateriaPrima] = useState('');

    useEffect(() => {
        axios.get('https://sistema-web-v.onrender.com/sistema/dropdown_proveedores/')
            .then(response => setProveedores(response.data))
            .catch(error => console.error(error));
        
        axios.get('https://sistema-web-v.onrender.com/sistema/dropdown_materias_primas/')
            .then(response => setMateriasPrimas(response.data))
            .catch(error => console.error(error));
    }, []);

    
    const handleSearch = () => {
        axios.post('https://sistema-web-v.onrender.com/sistema/proveedor_materia_prima/', {
            denominacion_social: selectedProveedor,
            nombre: selectedMateriaPrima
        }).then(response => setRows(response.data))
          .catch(error => console.error(error));
    };

    const columns = [
        { field: 'materia_prima', headerName: 'Materia Prima', width: 200 },
        { field: 'proveedor', headerName: 'Proveedor', width: 200 },
        { field: 'cantidad_lotes', headerName: 'Cantidad de Lotes', width: 200 },
    ];

    return (
        <div>
            <FormControl>
                <InputLabel>Proveedor</InputLabel>
                <Select
                    value={selectedProveedor}
                    onChange={e => setSelectedProveedor(e.target.value)}
                >
                    {proveedores.map((prov, index) => (
                        <MenuItem key={index} value={prov.denominacion_social}>
                            {prov.denominacion_social}
                        </MenuItem>
                    ))}
                </Select>
                <Button onClick={handleSearch}>Buscar</Button>
            </FormControl>

            <FormControl>
                <InputLabel>Materia Prima</InputLabel>
                <Select
                    value={selectedMateriaPrima}
                    onChange={e => setSelectedMateriaPrima(e.target.value)}
                >
                    {materiasPrimas.map((mat, index) => (
                        <MenuItem key={index} value={mat.nombre}>
                            {mat.nombre}
                        </MenuItem>
                    ))}
                </Select>
                <Button onClick={handleSearch}>Buscar</Button>
            </FormControl>

            <div style={{ height: 400, width: '100%' }}>
                <DataGrid rows={rows} columns={columns} pageSize={5} />
            </div>
        </div>
    );
};

export default LotesAlmacen;
