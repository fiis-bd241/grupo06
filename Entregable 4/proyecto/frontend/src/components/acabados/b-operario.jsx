import React from 'react';
import { FormControl, InputLabel, Select, MenuItem } from '@mui/material';
import { useEffect, useState } from "react";
import axios from "axios";
const IDDropdown = () => {
  const [idOperario, setIdOperario] = React.useState('');

  const handleChange = (event) => {
    setIdOperario(event.target.value);
  };

//dropdown
const [empleados, setEmpleados] = useState([]);

useEffect(() => {
    axios.get("https://sistema-web-v.onrender.com/sistema/empleados")
        .then(response => setEmpleados(response.data))
        .catch(error => console.error('Error fetching empleados:', error));
}, []);



  return (
    <FormControl variant="outlined" fullWidth>
      <InputLabel id="id-operario-label">ID Operario</InputLabel>
      <Select
        labelId="id-operario-label"
        id="id-operario-select"
        value={idOperario}
        onChange={handleChange}
        label="ID Operario"
      >
      {empleados.map((empleado) => (
        <MenuItem key={empleado.id_empleado} value={empleado.id_empleado}>
        {empleado.id_empleado}
        </MenuItem>

      ))}
      </Select>
    </FormControl>
  );
};

export default IDDropdown;
