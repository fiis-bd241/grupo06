// AcabadoList.js

import React, { useState, useEffect } from 'react';
import axios from 'axios';

const AcabadoList = () => {
  const [acabados, setAcabados] = useState([]);

  useEffect(() => {
    const fetchAcabados = async () => {
      try {
        const response = await axios.get('https://sistema-web-v.onrender.com/sistema/acabados/');
        setAcabados(response.data);
      } catch (error) {
        console.error('Error fetching acabados:', error);
      }
    };

    fetchAcabados();
  }, []);

  return (
    <div>
      <ul>
        {acabados.map(acabado => (
          <li key={acabado.id_acabado}>{acabado.nombre}</li>
        ))}
      </ul>
    </div>
  );
};

export default AcabadoList;
