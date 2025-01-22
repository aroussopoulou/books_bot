# Book Discovery Chatbot
## Domain and Motivation
The Book Discovery Chatbot is designed to help users find book recommendations, fetch synopses, retrieve detailed information, and explore bestseller lists. The motivation behind choosing this domain includes:

**Passion for Books:** It combines a love for literature with technology, creating a helpful assistant for avid readers.

**Practical Utility:** Users can quickly access book details and recommendations without manually browsing online sources.

**Real-world Data Integration:** The chatbot dynamically fetches data from reputable sources like Google Books and the New York Times, ensuring up-to-date and accurate information.

## Implemented Scenarios
The chatbot demonstrates distinct functionalities through various interaction scenarios:

### 1. Searching for Books with Pagination

**Use Case:** Users can search for books by author, genre, or keyword.
Functionality:
The bot fetches an initial list of five books based on the user's **query**.
It supports pagination: when the user types **"more books,"** it retrieves additional results.

**Demonstration:**

Your input ->  hello

Hello there! Looking for book recommendations, reviews, or details?

Your input ->  Show me books in the horror genre

Here are some books I found:
- Tales from the Shadowhunter Academy
- Misery
- Four Past Midnight
- Frankenstein
- The Dream-quest of Unknown Kadath
Type 'more books' if you'd like to see additional results.

Your input ->  more books

Here are some books I found:
- Frankenstein by Mary Wollstonecraft Shelley
- The Secret Path by Christopher Pike
- Thinner by Stephen King, Richard Bachman
- The Waste Lands by Stephen King
- Ring by Kōji Suzuki
Type 'more books' if you'd like more results.
Do you need any further help with books?

### 2. Retrieving Book Synopsis

**Use Case:** Users can request a synopsis of a specific book.

**Functionality:** The bot uses the Google Books API to fetch and display a book's synopsis.

**Demonstration:**

Your input ->  What's the description for Frankenstein by Mary Wollstonecraft Shelley

Synopsis of *the description for Frankenstein by Mary Wollstonecraft Shelley*:
"Everything about Mary Shelley's Frankenstein is remarkable!" -Sidney Perkowitz ; LA Review of Books Frankenstein; or, The Modern Prometheus is a novel written by English author Mary Shelley (1797-1851) that tells the story of Victor Frankenstein, a young scientist who creates a hideous sapient creature in an unorthodox scientific experiment. Frankenstein is infused with elements of the Gothic novel and the Romantic movement. Brian Aldiss has argued that it should be considered the first true science fiction story because, in contrast to previous stories with fantastical elements resembling those of later science fiction, the central character "makes a deliberate decision" and "turns to modern experiments in the laboratory" to achieve fantastic results. It has had a considerable influence in literature and popular culture and spawned a complete genre of horror stories, films and plays. A True Classic that Belongs on Every Bookshelf!
Do you need any further help with books?

### 3. Fetching Book Details

**Use Case:** Users can ask for detailed information about a book.

**Functionality:** The bot retrieves authors, publisher, publication date, and a link for more info using the Google Books API.

**Demonstration:**
Your input ->  Give me details about Frankenstein by Mary Wollstonecraft Shelley

📖 *Title*: Φρανκενστά: Frankenstein, Greek Edition
🖋️ *Author(s)*: Mary Shelley
🏢 *Publisher*: Mollusca Press
📅 *Published Date*: 2018-12-08
🔗 *More Info*: [Click here](http://books.google.gr/books?id=hgvZvwEACAAJ&dq=Give+me+details+about+Frankenstein+by+Mary+Wollstonecraft+Shelley&hl=&source=gbs_api)
Do you need any further help with books?

### 4. Listing Current Bestsellers

**Use Case:** Users inquire about trending books.

**Functionality:** The bot fetches and displays a list of current hardcover fiction bestsellers using the New York Times Books API.

**Demonstration:**

Your input ->  Show me the bestseller list
Here are the current bestsellers in hardcover fiction:

📚 Title: IRON FLAME

🖋️ Author: Rebecca Yarros

💡 Description: The second book in the Empyrean series. Violet Sorrengail’s next round of training under the new vice commandant might require her to betray the man she loves.

🔗 Buy here: https://www.amazon.com/dp/1649374178?tag=thenewyorktim-20


📚 Title: JAMES

🖋️ Author: Percival Everett

💡 Description: A reimagining of “Adventures of Huckleberry Finn” shines a different light on Mark Twain's classic, revealing new facets of the character of Jim.

🔗 Buy here: https://www.amazon.com/dp/0385550367?tag=thenewyorktim-20


📚 Title: THE WOMEN

🖋️ Author: Kristin Hannah

💡 Description: In 1965, a nursing student follows her brother to serve during the Vietnam War and returns to a divided America.

🔗 Buy here: https://www.amazon.com/dp/1250178630?tag=thenewyorktim-20


📚 Title: FOUR RUINED REALMS

🖋️ Author: Mai Corland

💡 Description: The second book in the Broken Blades series. Trust is tested in the pursuit of the Golden Ring of the Dragon Lord.

🔗 Buy here: https://www.amazon.com/dp/1649377509?tag=thenewyorktim-20


📚 Title: NEVER SAY NEVER

🖋️ Author: Danielle Steel

💡 Description: A woman reeling from her husband’s infidelity and the loss of her job meets a well-known actor in the French countryside.

🔗 Buy here: https://www.amazon.com/dp/059349864X?tag=thenewyorktim-20


📚 Title: THE GOD OF THE WOODS

🖋️ Author: Liz Moore

💡 Description: When a 13-year-old girl disappears from an Adirondack summer camp in 1975, secrets kept by the Van Laar family emerge.

🔗 Buy here: https://www.amazon.com/dp/0593418913?tag=thenewyorktim-20


📚 Title: HOLMES IS MISSING

🖋️ Author: James Patterson and Brian Sitts

💡 Description: The second book in the Holmes, Margaret & Poe series. A series of child abductions perplexes the private investigators.

🔗 Buy here: https://www.amazon.com/dp/0316569976?tag=thenewyorktim-20

Do you need any further help with books?

## Data Source Integration

For the Book Discovery Chatbot, I selected two primary data sources: the Google Books API and the New York Times Books API. The choice of these datasets was driven by a desire to offer a rich, dynamic, and reliable user experience in exploring literature.

**Google Books API**
The Google Books API serves as a comprehensive database for searching books, fetching synopses, and retrieving detailed information. By integrating this API, the chatbot can access up-to-date metadata for millions of books—covering titles, authors, descriptions, publication details, and more. Custom actions in the bot call the Google Books API using HTTP requests, parse the returned JSON data, and present concise results to users. This enables functionalities like searching by author or genre, providing synopses, and displaying detailed book information. The rationale for choosing Google Books API lies in its breadth and reliability: it offers an extensive catalog of literature that ensures users receive accurate and current information, thereby fulfilling the chatbot's goal of aiding book discovery.

**New York Times Books API**
To complement the comprehensive data from Google Books, the New York Times Books API was chosen to retrieve curated bestseller lists. This API provides reliable, authoritative information on current trends in literature, especially within categories like hardcover fiction. A dedicated action (ActionBookBestSellers) fetches bestseller data, processes it, and presents it in a user-friendly format. The rationale here is twofold: the NYT Books API not only offers curated and timely recommendations from a trusted source but also enhances the chatbot’s credibility by tapping into a recognized authority on literary trends.

## Challenges and Solutions

### 1. Managing Dialogue Rules and Stories

**Challenge:** Integrating both Rasa rules and stories to handle actions caused conflicts. The system struggled to differentiate between strict rule-based responses and more flexible story-based conversation flows, leading to unpredictable behavior and difficulties in maintaining coherent dialogues.

**Solution:** To streamline conversation management, I chose to consolidate action handling exclusively into stories rather than mixing in separate rules for those actions. By doing so, I simplified the dialogue structure:

### 2. Large Model Size and GitHub Upload Constraints

**Challenge:** The model and associated files were too large for GitHub’s standard file size limits, particularly due to the extensive training data in nlu.yml. This made pushing the repository to GitHub difficult.

**Solution:** To reduce the model size and fit GitHub’s constraints:

Simplified nlu.yml: Removed some lines and less relevant training examples from nlu.yml to decrease the overall file size without compromising essential functionality.
Git LFS: Introduced Git Large File Storage (Git LFS) to handle large files if necessary, though simplifying the data was prioritized.
Impact:
The repository became small enough to upload to GitHub successfully while maintaining the core functionalities of the chatbot, but the bad news is that the sentences of the model that can be understood and recognized have decreased. 

### 3. Persisting Query Between Actions for Pagination

**Challenge:**In the action_load_more_books, the variable query was not preserved from the previous action_search_books. This meant that when the user requested more books, the chatbot lost the original search context, resulting in errors or incorrect behavior.

**Solution:** To maintain the search context across multiple actions:
Modified action_search_books to return the search query and initial offset as slot events:

return [
    {"event": "slot", "name": "search_query", "value": query},
    {"event": "slot", "name": "search_offset", "value": 5.0},
]

This ensured that search_query persisted in the conversation memory and could be accessed by action_load_more_books, allowing the chatbot to continue fetching the next set of books using the same query.

**Impact:** The chatbot now correctly carries over the search context across multiple "more books" requests, enabling a seamless pagination experience.

### 4. Domain Slot Configuration Issue

**Challenge:** There was a problem with the definition of the search_offset slot in the domain. Initially defined incorrectly or with insufficient configuration, this could cause slot persistence or type issues.

**Solution:** Updated the slot configuration in domain.yml to:

search_offset:
    type: float                   
    influence_conversation: false
    initial_value: 0.0            
    mappings: []
    
This configuration correctly defines the slot type, and initial value, and provides an empty mapping to satisfy Rasa's requirements.

### 5. Additional Model Design Considerations

The model is designed to address conversational challenges robustly:

**Handling Misunderstandings:** If the chatbot doesn't understand a user's input, it is equipped to ask clarifying questions or request rephrasing. This fallback mechanism ensures smoother conversations and helps guide users toward more understandable queries.

**Responding to Bot Challenges:** When a user states something like "I'm a bot" or questions the chatbot's nature, the model can recognize these inputs (using the bot_challenge intent) and respond appropriately. This feature helps maintain engagement and assures the user of the bot's capabilities and design intent.

## Setup Instructions

### 1. Clone the Repository

In your PowerShell write

 mkdir books_bot
 
 cd books_bot
 
 python -m venv venv # Create a virtual environment
 
 .\venv\Scripts\Activate
 
 git clone https://github.com/aroussopoulou/books_bot.git

 ### 2. Extract the API keys

 **GOOGLE API KEY**
 
 a) Go to the Google Cloud console 
 
 b) Sign in to your Google account (if it is your first time check this video: https://www.youtube.com/watch?v=KcHx5dXaDtk&ab_channel=CloudSprint)
 
 c) Go to the APIs and services
 
 d) Create credentials -> API key
 
 e) Go to the library and search **Books API**
 
 f) Press the enable button

 **NYT API KEY**

 You can follow these instructions: https://developer.nytimes.com/get-started

 a) Visit the site https://developer.nytimes.com/
 
 b) Create an account and sign in
 
 c) Go to the user drop-down and select My Apps
 
 d) Click + New App to create a new app and enter a name
 
 e) Click Create and after go to the APIs tab
 
 f) Select the access toggle to enable or disable access to an API product from the app
 
 g) Go to My Apps and after in the list you can see the API key

 ### 3. Use your API keys to the actions.py

 You can open the files in the VSCode environment and do copy-paste the API keys everywhere you see the "USE_GOOGLE_API_KEY" or "USE_NYT_API_KEY". You have to add it in five actions: **action_search_books, action_load_more_books, action_book_best_sellers, action_book_synopsis, action_book_details**

 ### 4. Run the bot

 You have to open a new tab in PowerShell and write:
 
 cd books_bot 
 
  .\venv\Scripts\Activate
  
  **rasa run actions**

  and in the tab that you were in before write:
  
  **rasa shell**
  
 If it doesn't work try training the bot first: **rasa train** and after doing the above steps

 ### 5. Interact with the Bot

Test different scenarios: searching books, loading more results, getting synopses, retrieving details, and checking bestsellers.

## Example runs

Your input ->  Hi!

Greetings! How can I assist you with books today?

Your input ->  Show me books in the romance genre

Here are some books I found:
- Pride and Prejudice
- Simple Gifts
- Pride and Prejudice
- Above and Beyond
- Last Sacrifice
Type 'more books' if you'd like to see additional results.

Your input ->  more books

Here are some books I found:
- Sons and Lovers by David Herbert Lawrence
- The Italian Girl by Lucinda Riley
- The Missing Sister by Lucinda Riley
- A Loving Scoundrel by Johanna Lindsey
- Love Only Once by Johanna Lindsey
Type 'more books' if you'd like more results.
Do you need any further help with books?

Your input ->  Tell me what Sons and Lovers by David Herbert Lawrence is about

Synopsis of *Tell me what Sons and Lovers by David Herbert Lawrence is about*:
This semi-autobiographical novel explores the emotional conflicts through the protagonist, Paul Morel, and the suffocating relationships with a demanding mother and two very different lovers.
Do you need any further help with books?

Your input ->  I'd like full info on Sons and Lovers by David Herbert Lawrence

📖 *Title*: D.H. Lawrence's Son and Lovers: A Critique
🖋️ *Author(s)*: D.S. Dalal
🏢 *Publisher*: Sarup & Sons
📅 *Published Date*: 2007-10
🔗 *More Info*: [Click here](http://books.google.gr/books?id=7T-06uA5C4cC&dq=like+full+info+on+Sons+and+Lovers+by+David+Herbert+Lawrence&hl=&source=gbs_api)
Do you need any further help with books?

Your input ->  Are you human?

I’m a virtual assistant created to help you explore the world of books!

Your input ->  Show me the bestseller list

Here are the current bestsellers in hardcover fiction:
📚 Title: IRON FLAME
🖋️ Author: Rebecca Yarros
💡 Description: The second book in the Empyrean series. Violet Sorrengail’s next round of training under the new vice commandant might require her to betray the man she loves.
🔗 Buy here: https://www.amazon.com/dp/1649374178?tag=thenewyorktim-20
📚 Title: JAMES
🖋️ Author: Percival Everett
💡 Description: A reimagining of “Adventures of Huckleberry Finn” shines a different light on Mark Twain's classic, revealing new facets of the character of Jim.
🔗 Buy here: https://www.amazon.com/dp/0385550367?tag=thenewyorktim-20
📚 Title: THE WOMEN
🖋️ Author: Kristin Hannah
💡 Description: In 1965, a nursing student follows her brother to serve during the Vietnam War and returns to a divided America.
🔗 Buy here: https://www.amazon.com/dp/1250178630?tag=thenewyorktim-20
📚 Title: FOUR RUINED REALMS
🖋️ Author: Mai Corland
💡 Description: The second book in the Broken Blades series. Trust is tested in the pursuit of the Golden Ring of the Dragon Lord.
🔗 Buy here: https://www.amazon.com/dp/1649377509?tag=thenewyorktim-20
📚 Title: NEVER SAY NEVER
🖋️ Author: Danielle Steel
💡 Description: A woman reeling from her husband’s infidelity and the loss of her job meets a well-known actor in the French countryside.
🔗 Buy here: https://www.amazon.com/dp/059349864X?tag=thenewyorktim-20
📚 Title: THE GOD OF THE WOODS
🖋️ Author: Liz Moore
💡 Description: When a 13-year-old girl disappears from an Adirondack summer camp in 1975, secrets kept by the Van Laar family emerge.
🔗 Buy here: https://www.amazon.com/dp/0593418913?tag=thenewyorktim-20
📚 Title: HOLMES IS MISSING
🖋️ Author: James Patterson and Brian Sitts
💡 Description: The second book in the Holmes, Margaret & Poe series. A series of child abductions perplexes the private investigators.
🔗 Buy here: https://www.amazon.com/dp/0316569976?tag=thenewyorktim-20
Do you need any further help with books?

Your input ->  No

No worries. Let me know if you need anything else.

Your input ->  goodbye

Take care and happy reading!

## Dialog Policy Experimentation

### 1. Adjusted Fallback Threshold:

In the RulePolicy, I set the core_fallback_threshold to 0.4 and specified core_fallback_action_name: "utter_clarify". Additionally, I configured the FallbackClassifier in the pipeline with a threshold of 0.4 and an ambiguities_threshold of 0.1. Increasing the fallback threshold helps the chatbot avoid making incorrect assumptions when it's not confident in the user's intent. By setting a specific fallback action (utter_clarify), the bot can ask the user to rephrase their query instead of providing irrelevant or incorrect responses. This makes the conversation smoother and more user-friendly.

### 2. Modified History Lengths and Training Epochs:

For the UnexpecTEDIntentPolicy, I set max_history: 5 and epochs: 100. For the TEDPolicy, I set max_history: 10 and epochs: 100. These adjustments aim to capture a longer context in conversations and allow more robust training, improving the model's understanding of multi-turn dialogues and rare/unexpected intents.

