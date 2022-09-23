import { useState } from 'react'

export const Form = () => {
    var twitterHandleGotten = ""
    var profilePicURL = "https://unavatar.io/twitter/"

    const [twitterHandleEntered, setTwitterHandle] = useState('')
    const [img, setImg] = useState();
    const [categoryList, setCategoryList] = useState();
    const [botScore, setBotScore] = useState();
    const [sentimentScore, setSentimentScore] = useState();
    const [tHandle, setTHandle] = useState();
    const [showResults, setShowResults] = useState(false);
    const [showResultsContent, setShowResultsContent] = useState(false);
    const [goodApi, setGoodApi] = useState(true);


    const requestOptions = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ twitterHandle:twitterHandleEntered })
    };

    const submitHandler = (event) => {
        event.preventDefault()
        fetch('https://ec463tweetometer.herokuapp.com/tweetometer', requestOptions)
            .then((response) => {
                if(response.ok){
                    setGoodApi(true)
                }
                else{
                    setGoodApi(false)
                }
                return response.json()
            })
            .then((json) => {
                console.log(json)
                twitterHandleGotten = json['twitterHandle'].substring(1)
                setImg(profilePicURL + twitterHandleGotten)
                setTHandle(json['twitterHandle'])
                setBotScore(json['botScore'])
                setCategoryList(json['categoryList'])
                var sentimentScoreGotten = json['sentimentScore']
                setSentimentScore(parseFloat(sentimentScoreGotten).toFixed(2))
                setShowResultsContent(true)
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
                <button className="twitterhandle-input-button" type='submit' onClick={()=> {setShowResults(true); setShowResultsContent(false); setGoodApi(true)}}>Analyze</button>
            </div>

            {
                goodApi ? showResults && 
                <div className="twitter-user-box">
                    { 
                        showResultsContent ? 
                        <div className="twitter-analysis-content">
                            <button type="button" className="close" aria-label="Close" onClick={()=> {setShowResults(false); setShowResultsContent(false)}}  >
                                <span aria-hidden="true">×</span>
                            </button>
                            <img className="user-image" src={ img } onError={(e) => (e.target.onerror = null, e.target.src = img)} alt=""/>
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
                                <p className="box-header-text"> Top Categories from { tHandle } </p>
                                    <div>
                                        {categoryList?.map((category, index) => (
                                            <p className="box-header-text" key={index}> {category[0] }</p>
                                        ))}
                                    </div>
                            </div>
                        </div> :  <div className="lds-ring"><div></div><div></div><div></div><div></div></div>
                    } 
                </div> : <p className="error-msg">An error occurred, either the user entered is invalid, or the user entered cannot be analyzed.</p>
            }  
         </form>
    )
}