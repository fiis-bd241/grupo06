import React from "react";
import { useState, useEffect } from "react";
import Sidenav from "../../components/Sidenav";
import Navbar from "../../components/Navbar";
import Box from "@mui/material/Box";

//navegation
import Navigation from "../../components/Navigation";
import Bot from "../../components/acabados/bot";

import DenseTable from "../../components/acabados/tabla-et";

import SkeletonLoader from "../SkeletonLoader"; // Importar el componente de skeleton

export default function Detalle() {
  //Skeleton
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Simula la carga de datos
    setTimeout(() => {
      setLoading(false);
    }, 1500); // Tiempo de espera simulado de 3 segundos
  }, []);

  return (
    <>
      <Navbar />
      <Box height={30} />
      <Box sx={{ display: "flex" }}>
        <Sidenav />

        <Box component="main" sx={{ flexGrow: 1, p: 3 }}>
          {loading ? (
            <SkeletonLoader /> // Mostrar el skeleton mientras se cargan los datos
          ) : (
            <>
              <h1>Área de Acabados</h1>
              <div>
                <Navigation />
              </div>

              <div className="App2">
                <div className="container">
                  <div className="field">
                    <label>ID CAJA:</label>
                    <span>006</span>
                  </div>
                  <div className="field">
                    <label>
                      <strong>Fecha de creación:</strong>
                    </label>
                    <span>13/05/2023</span>
                  </div>
                  <div className="field">
                    <label>Cantidad:</label>
                    <span>50</span>
                  </div>
                  <div className="field">
                    <label>Prenda:</label>
                    <span>Pantalón</span>
                  </div>
                </div>
              </div>
              <div>
                <Box display="flex" justifyContent="flex-end" mt={2}>
                  <Bot />
                </Box>
                <DenseTable />{" "}
              </div>
            </>
          )}
        </Box>
      </Box>
    </>
  );
}
