import { Form } from './Form'
export const WelcomeBody = () => {
    return (
          <div className="welcome-body">
            <h1 className="welcome-text"> Welcome to Tweetometer! </h1>
            <h2 className="welcome-text"> EC463 Mini Project </h2>
            <div className="welcome-instructions-box">
                <p className="instruction-text">Tweetometer is a tool that performs sentiment analysis. </p>
                <p className="instruction-text">It checks if a twitter user has a bot account or is a human. </p>
                <p className="instruction-text">It shows the topics talked about in their tweet history.</p>
            </div>
            <h2 className="typehandle-text"> Enter a Twitter Handle Below to Get Started </h2>
            <Form />
          </div>
      );
}