import { useEffect, useState } from "react";

function App() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/store/products/")
      .then(res => res.json())
      .then(data => {
        console.log("API RESPONSE:", data);

        let productsArray = [];

        if (Array.isArray(data)) {
          productsArray = data;
        } else if (Array.isArray(data.results)) {
          productsArray = data.results;
        }

        setProducts(productsArray);
      })
      .catch(err => console.log("FETCH ERROR:", err));
  }, []);

  return (
    <div>
      <h1>Products</h1>

      {Array.isArray(products) &&
        products.map(product => (
          <div key={product.id}>
            <h3>{product.title}</h3>
            <p>R{product.unit_price}</p>
          </div>
        ))
      }
    </div>
  );
}

export default App;