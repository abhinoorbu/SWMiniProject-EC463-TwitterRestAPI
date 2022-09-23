import React, { useState, useEffect } from "react";

export const Navbar = () => {
  const [sticky, setSticky] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      setSticky(window.scrollY > 0);
    //   console.log(window.scrollY);
    };
    window.addEventListener("scroll", handleScroll);
    return () => window.removeEventListener("scroll", handleScroll);
  });
  return (
    <nav className={`${sticky ? "sticky" : ""}`}>
      <div className="nav-inner">
        <img className="twitterLogo" src={require('../twitterLogo.png')} alt="twitter logo"/>
        {/* <span className="title">Tweetometer</span> */}
        <h1 className="title"> Tweetometer </h1>
      </div>
    </nav>
  );
}
