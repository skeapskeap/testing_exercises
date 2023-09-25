import pytest

from functions.level_2.four_sentiment import check_tweet_sentiment


@pytest.mark.parametrize("text, good_words, bad_words", [
    pytest.param("text without matching words", {"good_word"}, {"bad_word"}, id="no matches"),
    pytest.param("random text", {}, {}, id="empty good and bad words"),
    pytest.param("", {"good_word"}, {"bad_word"}, id="empty text"),
])
def test__check_tweet_sentiment__no_matches(text, good_words, bad_words):
    assert check_tweet_sentiment(text, good_words, bad_words) is None


@pytest.mark.parametrize("text", [
    "good_word_1 bad_word_1",
    "good_word_1 good_word_2 bad_word_1 bad_word_2",
    "good_word_1 good_word_1 bad_word_1 bad_word_1",
])
def test__check_tweet_sentiment__good_words_equals_bad_words(text):
    good_words = {"good_word_1", "good_word_2"}
    bad_words = {"bad_word_1", "bad_word_2"}
    assert check_tweet_sentiment(text, good_words, bad_words) is None


@pytest.mark.parametrize("text", [
    "good_word_1",
    "good_word_1 good_word_1 bad_word",
    "good_word_1 good_word_2 bad_word",
])
def test__check_tweet_sentiment__good_sentiment(text):
    good_words = {"good_word_1", "good_word_2"}
    bad_words = {"bad_word"}
    assert check_tweet_sentiment(text, good_words, bad_words) == "GOOD"


@pytest.mark.parametrize("text", [
    "bad_word_1",
    "good_word bad_word_1 bad_word_1",
    "good_word bad_word_1 bad_word_2",
])
def test__check_tweet_sentiment__bad_sentiment(text):
    good_words = {"good_word"}
    bad_words = {"bad_word_1", "bad_word_2"}
    assert check_tweet_sentiment(text, good_words, bad_words) == "BAD"
