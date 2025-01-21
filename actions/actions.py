import os
import requests
from typing import Any, Text, Dict, List, Optional
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

def get_env_var(name: str, default: str = "") -> str:
    """Retrieve an environment variable or return a default value if not set."""
    return os.environ.get(name, default)

# Mockup Function
class ActionShowRecommendations(Action):
    def name(self) -> Text:
        return "action_show_recommendations"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Predefined list of book recommendations
        recommendations = [
            "1984 by George Orwell",
            "Pride and Prejudice by Jane Austen"
        ]
        dispatcher.utter_message(
            text=f"Here are some recommended books: {', '.join(recommendations)}"
        )
        return []
    
# 1) SEARCH BOOKS (initial 5) - unchanged
class ActionSearchBooks(Action):
    def name(self) -> Text:
        return "action_search_books"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        # Retrieve entities from the tracker
        author = tracker.get_slot("author")
        genre = tracker.get_slot("genre")
        keyword = tracker.get_slot("keyword")

        # Use your known working code to search books initially
        query = ""
        if author:
            query += f"+inauthor:{author}"
        if genre:
            query += f"+subject:{genre}"
        if keyword:
            query += f"+{keyword}"

        api_key = "AIzaSyCFPALEff2_bmC4EDrpMob7-Fij7yVCmOM"
        url = f"https://www.googleapis.com/books/v1/volumes?q={query}&key={api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            books_data = response.json()
            books = books_data.get("items", [])
            if not books:
                dispatcher.utter_message(text="Sorry, I couldn't find any books matching your criteria.")
                return []

            book_titles = [book["volumeInfo"].get("title", "Unknown Title") for book in books[:5]]
            dispatcher.utter_message(text=f"Here are some books I found:\n" + "\n".join(f"- {title}" for title in book_titles))
            dispatcher.utter_message(text="Type 'more books' if you'd like to see additional results.")
            # Store the search query and set initial offset for pagination
            return [
                {"event": "slot", "name": "search_query", "value": query},
                {"event": "slot", "name": "search_offset", "value": 5.0},
            ]
        except requests.exceptions.RequestException as e:
            dispatcher.utter_message(text="Sorry, I couldn't fetch the books at the moment. Please try again later.")
            print(f"Error fetching books: {e}")
            return []

# 2) SEARCH MORE BOOKS 
class ActionLoadMoreBooks(Action):
    def name(self) -> Text:
        return "action_load_more_books"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        query = tracker.get_slot("search_query")
        offset = tracker.get_slot("search_offset") or 0.0
        offset = int(offset)

        # Debug prints to check slot values
        print(f"DEBUG: search_query = {query}, search_offset = {offset}")

        if not query:
            dispatcher.utter_message(
                text="I don't have a saved search query. Try searching for books first."
            )
            return []

        max_results = 5
        api_key = "AIzaSyCFPALEff2_bmC4EDrpMob7-Fij7yVCmOM"  # Use your API key here

        # Use a clean base URL without embedded parameters
        url = "https://www.googleapis.com/books/v1/volumes"

        # Pass all parameters through the params dictionary
        params = {
            "q": query,
            "key": api_key,
            "startIndex": offset,
            "maxResults": max_results,
        }

        try:
            resp = requests.get(url, params=params, timeout=5)
            resp.raise_for_status()
            data = resp.json()
            items = data.get("items", [])

            if not items:
                dispatcher.utter_message(text="No more books found for your search.")
                return []

            titles = []
            for item in items:
                volume = item.get("volumeInfo", {})
                title = volume.get("title", "Unknown Title")
                authors = volume.get("authors", ["Unknown Author"])
                authors_str = ", ".join(authors)
                titles.append(f"{title} by {authors_str}")

            joined_titles = "\n- " + "\n- ".join(titles)
            dispatcher.utter_message(
                text=f"Here are some books I found:\n{joined_titles}"
            )

            new_offset = float(offset + max_results)

            dispatcher.utter_message(text="Type 'more books' if you'd like more results.")

            return [
                {"event": "slot", "name": "search_offset", "value": new_offset},
            ]

        except requests.exceptions.RequestException as e:
            dispatcher.utter_message(
                text="Sorry, I couldn't fetch books at the moment. Please try again later."
            )
            print(f"Error fetching books: {e}")
            return []

# 3) BESTSELLERS (NYT)
class ActionBookBestSellers(Action):
    def name(self) -> Text:
        return "action_book_best_sellers"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        

        api_key = "vqFV7OdOKE51Dy5CUFLJrk2GcREy4BeG"

        url = f"https://api.nytimes.com/svc/books/v3/lists/current/hardcover-fiction.json?api-key={api_key}"

        try:
            resp = requests.get(url, params={"api-key": api_key}, timeout=5)
            resp.raise_for_status()
            data = resp.json()
            results = data.get("results", {})
            books = results.get("books", [])

            if not books:
                dispatcher.utter_message(
                    text="Couldn't retrieve the bestseller list right now."
                )
                return []

            dispatcher.utter_message(text="Here are the current bestsellers in hardcover fiction:")
            # Show top 10
            for book in books[:7]:
                title = book.get("title", "Unknown Title")
                author = book.get("author", "Unknown Author")
                description = book.get("description", "No description available.")
                buy_link = book.get("amazon_product_url", "No link available.")
                message = (
                    f"📚 Title: {title}\n"
                    f"🖋️ Author: {author}\n"
                    f"💡 Description: {description}\n"
                    f"🔗 Buy here: {buy_link}"
                )
                dispatcher.utter_message(text=message)

        except requests.exceptions.RequestException as e:
            dispatcher.utter_message(
                text="Error fetching the NYT bestseller list. Please try again later."
            )
            print(f"Error: {e}")

        return []


# 4) BOOK SYNOPSIS (just description)
class ActionBookSynopsis(Action):
    def name(self) -> Text:
        return "action_book_synopsis"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        book_title = tracker.get_slot("book_title")
        if not book_title:
            dispatcher.utter_message(text="Please specify which book you want a synopsis for.")
            return []

        api_key = "AIzaSyCFPALEff2_bmC4EDrpMob7-Fij7yVCmOM"
        # Use book_title in the query
        url = "https://www.googleapis.com/books/v1/volumes"
        params = {
            "q": f"intitle:{book_title}",
            "key": api_key,
            "maxResults": 1
        }

        try:
            resp = requests.get(url, params=params, timeout=5)
            resp.raise_for_status()
            data = resp.json()
            items = data.get("items", [])

            if not items:
                dispatcher.utter_message(text=f"Sorry, I couldn't find a synopsis for '{book_title}'.")
                return []

            volume_info = items[0].get("volumeInfo", {})
            description = volume_info.get("description", "No description available.")
            dispatcher.utter_message(text=f"Synopsis of *{book_title}*:\n{description}")

        except requests.exceptions.RequestException as e:
            dispatcher.utter_message(text="Error reaching Google Books. Please try again later.")
            print(f"API Error: {e}")

        return []


# 5) BOOK DETAILS (author, publisher, date, link, no description)
class ActionBookDetails(Action):
    def name(self) -> Text:
        return "action_book_details"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        book_title = tracker.get_slot("book_title")
        if not book_title:
            dispatcher.utter_message(
                text="Please specify which book you want details for."
            )
            return []
        
        api_key = "AIzaSyCFPALEff2_bmC4EDrpMob7-Fij7yVCmOM"
        # Use book_title in the query
        url = "https://www.googleapis.com/books/v1/volumes"
        params = {
            "q": f"intitle:{book_title}",
            "key": api_key,
            "maxResults": 1
        }

        try:
            resp = requests.get(url, params={"q": book_title, "key": api_key, "maxResults": 1}, timeout=5)
            resp.raise_for_status()
            data = resp.json()
            items = data.get("items", [])

            if not items:
                dispatcher.utter_message(
                    text=f"Sorry, I couldn't find details for '{book_title}'."
                )
                return []

            volume_info = items[0].get("volumeInfo", {})
            title = volume_info.get("title", "Unknown Title")
            authors = volume_info.get("authors", ["Unknown Author"])
            publisher = volume_info.get("publisher", "Unknown Publisher")
            published_date = volume_info.get("publishedDate", "Unknown Date")
            info_link = volume_info.get("infoLink", "No link available.")

            msg = (
                f"📖 *Title*: {title}\n"
                f"🖋️ *Author(s)*: {', '.join(authors)}\n"
                f"🏢 *Publisher*: {publisher}\n"
                f"📅 *Published Date*: {published_date}\n"
                f"🔗 *More Info*: [Click here]({info_link})"
            )
            dispatcher.utter_message(text=msg)

        except requests.exceptions.RequestException as e:
            dispatcher.utter_message(
                text="Error reaching Google Books. Please try again later."
            )
            print(f"API Error: {e}")

        return []