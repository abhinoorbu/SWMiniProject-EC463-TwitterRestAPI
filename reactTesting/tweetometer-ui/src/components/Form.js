import { useState } from 'react'

export const Form = () => {
    var twitterHandleGotten = ""
    var profilePicURL = "https://unavatar.io/twitter/"

    const [twitterHandleEntered, setTwitterHandle] = useState('')
    const [img, setImg] = useState();

    const [tweetList, setTweetList] = useState();
    const [categoryList, setCategoryList] = useState();
    const [botScore, setBotScore] = useState();
    const [sentimentScore, setSentimentScore] = useState();
    const [tHandle, setTHandle] = useState();


    const requestOptions = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ twitterHandle:twitterHandleEntered })
    };

    const submitHandler = (event) => {
        event.preventDefault()
        fetch('https://ec463tweetometer.herokuapp.com/tweetometer', requestOptions)
            .then((response) => response.json())
            .then((json) => {
                console.log(json)
                twitterHandleGotten = json['twitterHandle'].substring(1)
                setImg(profilePicURL + twitterHandleGotten)
                setTHandle(json['twitterHandle'])
                setTweetList(json['tweet'])
                setBotScore(json['botScore'])
                setCategoryList(json['categoryList'])
                var sentimentScoreGotten = json['sentimentScore']
                setSentimentScore(parseFloat(sentimentScoreGotten).toFixed(2))
            })
    }
    return (
        <form onSubmit={submitHandler}>
            <div>
                <input 
                    className="input-box-twitterhandle"
                    type="text" 
                    placeholder='@twitterhandle' 
                    value={ twitterHandleEntered } 
                    onChange={(e) => setTwitterHandle(e.target.value)}
                />
                <button className="twitterhandle-input-button" type='submit'>Analyze</button>
            </div>
            <div className="twitter-user-box">
                <img className="user-image" src={ img } alt="twitter profile img"/>
                <h1 className="twitter-handle-text"> { tHandle } </h1>
                {/* <h1 className="twitter-handle-text"> @mkbhd </h1> */}
                <div className="info-box">
                    <p className="box-header-text"> Botometer Score </p>
                    {/* <p className="box-content-text"> 0.21</p> */}
                    <p className="box-content-text"> { botScore }</p>
                </div>

                <div className="info-box">
                    <p className="box-header-text"> Sentiment Score </p>
                    {/* <p className="box-content-text"> 0.21</p> */}
                    <p className="box-content-text"> { sentimentScore }</p>
                </div>

                <div className="info-box-large">
                    <p className="box-header-text"> { tHandle }'s Top Categories</p>
                    <p className="box-content-text"> { categoryList }</p>
                </div>

            </div>  
         </form>
          
    )
}