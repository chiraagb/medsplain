"use client";

import { useEffect } from "react";
import Image from "next/image";

export default function Home() {
  useEffect(() => {
    if (localStorage.getItem("variable") !== "f") {
      window.alert("This is a popup");
    }
    localStorage.setItem("variable", "f");
  }, []); // Runs only once when the component mounts

  return (
    <>
      <div>Welcome to the Home Page</div>
    </>
  );
}
