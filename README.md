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
