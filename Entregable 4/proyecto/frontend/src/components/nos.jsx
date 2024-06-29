import React from 'react';
import "../estilos/home.css";
const Nos = () => {
  return (
    <div className='nos-container'>
    <h2>Nosotros</h2>
      <section>
        <h3>Nuestra Misión</h3>
        <p>
        Nuestra misión es establecer un estándar ejemplar en la industria textil y de confección al combinar la excelencia en la calidad, la flexibilidad en la producción y el cumplimiento riguroso de los plazos, todo ello respaldado por un compromiso inquebrantable con la generación de empleo y el desarrollo socioeconómico de nuestro país.
        </p>
      </section>
      <section>
        <h3>Nuestra Visión</h3>
        <p>
        En un plazo de cinco años, Vitex se visualiza como el líder indiscutible en la mente de nuestros compradores. Siendo elegidos por nuestra capacidad excepcional para entender, atender y superar las expectativas de nuestros clientes en términos de tiempos de entrega, flexibilidad y calidad de producto , contribuyendo de manera significativa al crecimiento del mercado textil y de confecciones de exportación peruano.
        </p>
      </section>
      <section>
        <a href="https://www.vircatex.com/" target="_blank" rel="noopener noreferrer">
          Visita nuestro sitio web.
        </a>
      </section>
    </div>
  );
}

export default Nos;
