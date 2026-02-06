---
layout: default-full
title: "Home"
subtitle: ""
vega: True
show_sidetoc: true
header_type: hero #base, post, hero,image, splash
header_img: assets/images/Microphone.jpg
header_title: "YouTube and Podcasts: <br>
The Rise of a New Era of Digital Content"
# subtitle: "How has the podcast world changed over the last 10 years?"
---

<!-- Custom width and offset -->
<div class="custom-col custom-offset"> </div>

<style>
    .quote-box {
        border: 2px solid #ccc;
        padding: 35px;
        margin: 35px 0; 
        background-color: #181818;
        font-style: italic;
        position: relative;
        outline: 2px solid #888;
        border-radius: 12px; /* Rounded outline */
        pointer-events: none; /* Ensure the element is not clickable */
        color: white;
    }
    .quote-box::before {
        content: "“";
        font-size: 4em;
        position: absolute;
        left: 10px;
        top: -10px;
        right: -10px;
        color: #ccc;
    }
    .quote-box::after {
        content: "”";
        font-size: 4em;
        position: absolute;
        right: 25px;
        bottom: 20px;
        color: #ccc;
    }
    .author {
        text-align: right;
        font-weight: bold;
        margin-top: 20px;
        color: white;
    }
    .container {
        position: relative;
        width: 100%;
        max-width: 800px;
        margin: 20px auto;
    }

    .collapsible {
        background: linear-gradient(45deg, 
                                    transparent 0%, 
                                    transparent 47%, 
                                    rgba(255, 255, 255, 0.3) 50%,
                                    rgba(255, 255, 255, 0.35) 51%,
                                    rgba(255, 255, 255, 0.40) 52%,
                                    rgba(255, 255, 255, 0.40) 53%,
                                    rgba(255, 255, 255, 0.35) 54%,
                                    rgba(255, 255, 255, 0.3) 55%, 
                                    transparent 58%, 
                                    transparent 100%);
        background-size: 200% 200%;
        background-position: 0% 100%;
        color: #ffffff;
        cursor: pointer;
        padding: 10px;
        width: auto;
        height: auto;
        border: none;
        text-align: center;
        outline: none;
        font-size: 16px;
        border-radius: 5px;
        transform-origin: right top;
        transform: rotate(0deg);
        transition: transform 0.3s;
        display: inline-block;
        animation: slideBackground 2s infinite linear;
    }

    .collapsible:focus {
        outline: none;
        border: none;
    }

    .collapsible.active {
        transform: rotate(-90deg);
        animation: none; /* Disable animation when active */
    }

    .content {
        padding: 20px;
        display: none;
        overflow: hidden;
        background-color: rgba(24, 24, 24, 0.8); /* Black with 80% opacity */
        color: #ffffff;
        border-radius: 5px;
        border: 1px solid #ccc;
        margin-top: -50px;
    }

    .header {
        display: flex;
        justify-content: flex-end;
    }

    .anchor-offset {
    scroll-margin-top: 90px; /* Add extra space above section */
    }

    @keyframes slideBackground {
        0% {
            background-position: 200% 100%;
        }
        100% {
            background-position: 0% 100%;
    }
}
</style>

<script>
    document.addEventListener('DOMContentLoaded', (event) => {
        var coll = document.getElementsByClassName("collapsible");
        for (var i = 0; i < coll.length; i++) {
            coll[i].addEventListener("click", function() {
                this.classList.toggle("active");
                var content = this.parentElement.nextElementSibling;
                if (content.style.display === "block") {
                    content.style.display = "none";
                } else {
                    content.style.display = "block";
                }
            });
        }
    });
</script>

<div id="introduzione" class="anchor-offset" style="text-align: center;">
    <h1 style="color: white; font-size: 48px;">Introduction</h1>
</div>

<div style="position: relative; width: 100%; padding-right: 200px; padding-left: 200px;">
    <div class="row">
        <div class="col-md-3 col-md-offset-3">
        </div>
        <div class="col-md-6">
            <hr>

            <p>Podcasts have moved from a niche format to a mainstream media habit—especially as YouTube has become a primary distribution layer for long-form, conversational content.</p>

            <p>The term <em>podcasting</em> emerged in the early 2000s, when RSS feeds made it easy to distribute downloadable MP3 audio to computers and portable devices. A widely cited turning point is Ben Hammersley’s 2004 <em>The Guardian</em> article <em>“Audible Revolution”</em>, which tried to name the growing phenomenon of portable, digitally scheduled audio outside traditional broadcast radio.</p>

            <p>Over the past decade, frictionless streaming, expanding creator tooling, and platform consolidation—Spotify first, YouTube later—have turned podcasts into a staple of the modern “media diet.”</p>

            <p>In Italy, this growth is measurable: IPSOS (2023) reports that <strong>39%</strong> of Italians listened to podcasts in the previous month—about <strong>11.9 million</strong> monthly listeners.</p>

            <p>Daria Corrias, radio author and documentary producer, described the early phase of the medium in our interview:</p>

            <div class="quote-box">
                "At the beginning there were many doubts and endless discussions about whether this 'podcast' could really be a viable format. We all started from <em>Serial</em>, which shaped what people thought a podcast should be: serialized, true-crime, and driven by a strong host voice. That was the podcast."
                <div class="author">- Daria Corrias</div>
            </div>

            <p>In those early years, podcasts were often <strong>horizontal</strong>: to fully understand an episode, you typically had to hear the previous one. Today, most shows are <strong>vertical</strong>—episodes stand on their own, making discovery and casual listening easier. The channels in our dataset largely follow this vertical model.</p>

            <div class="quote-box">
                Ten years after <em>Serial</em>, we can clearly see that podcasting is not just that.
                <div class="author">- Daria Corrias</div>
            </div>

            <p>For this project, we focused on the United States and selected <strong>24</strong> of the most-followed podcast channels on YouTube in <strong>May 2024</strong>, based on the public ranking available at <a title="Link" href="https://rephonic.com/charts/youtube/united-states/popular-podcasts" target="blank">this link</a>.</p>

            <p>Across these channels, we collected metadata for <strong>13,756</strong> episodes (views, likes, duration, publication date, and more), retrieved <strong>13,218</strong> transcripts via YouTube APIs, processed ~<strong>2,765 hours</strong> of audio, and analyzed more than <strong>18 million</strong> comments. This enabled a multi-layer view of performance: publishing cadence, topic evolution, sentiment, audio design, and visual strategy.</p>

            <br>

            <h4 style="text-align: center;">Chart 1: Descriptive statistics for the analyzed podcasts</h4>
            <p style="text-align: center;">A cross-reading of the charts suggests that the channels with the highest average views are not necessarily the most prolific. Performance likely reflects a combination of factors—such as average episode duration, subscriber base, and consistency of publishing.</p>
            <vegachart schema-url="{{site.baseurl}}/assets/charts/combined_chart_ulteriore.json" style="width: 100%; display: flex; justify-content: center;"></vegachart>

            <br>
            <br>
            <br>

            <h4 style="text-align: center;">Chart 2: Percentage distribution of podcasts in the dataset</h4>
            <p style="text-align: center;">This chart breaks down how episodes distribute over time. The pattern hints at seasonality and uneven publication intensity across the year.</p>
            <vegachart schema-url="{{site.baseurl}}/assets/charts/area_chart_podcast_distribution_dataset_black.json" style="width: 100%; display: flex; justify-content: center;"></vegachart>

            <br>
            <br>

            <h4 style="text-align: center;">Chart 3: Distribution of log-views by channel</h4>
            <p style="text-align: center;">Using a log scale, the chart highlights each channel’s best- and worst-performing episodes, revealing the typical gap between breakout hits and baseline performance.</p> 
            <vegachart schema-url="{{site.baseurl}}/assets/charts/std_views_podcast_chart_leggero.json" style="width: 100%; display: flex; justify-content: center;"></vegachart>

            <br>
            <br>

            <h4 style="text-align: center;">Chart 4: Views per channel over time</h4>
            <p style="text-align: center;">Each point represents an episode in chronological order; point size reflects views. The visualization makes it easy to spot spikes, consistent performers, and long-tail dynamics.</p> 
            <vegachart schema-url="{{site.baseurl}}/assets/charts/beeswarm_chart_leggero.json" style="width: 100%; display: flex; justify-content: center;"></vegachart> 

            <br>
            <br>

            <h4 style="text-align: center;">Chart 5: Total views and publications by month</h4>
            <p style="text-align: center;">By publication month, January contains the highest total views, while July shows the lowest. March records the largest number of releases; June the fewest—suggesting that release volume and view volume do not always move together.</p> 
            <vegachart schema-url="{{site.baseurl}}/assets/charts/views_pub_chart_BLACK_VERO 2.json" style="width: 100%; display: flex; justify-content: center;"></vegachart>                

            <br>
            <br>

            <h4 style="text-align: center;">Chart 6: Average number of published podcasts over time</h4>
            <p style="text-align: center;">The time series tracks the average publishing level across the dataset. By 2024, the mean reaches roughly <strong>13</strong> episodes (per the time unit used in the chart), reflecting sustained growth in output.</p> 
            <vegachart schema-url="{{site.baseurl}}/assets/charts/temporal_chart 2.json" style="width: 80%; height: 100vh;"></vegachart>

            <h4 style="text-align: center; margin-top: -80px;">Chart 7: Publication frequency</h4>
            <p style="text-align: center;">This chart estimates the probability of observing a given publishing frequency (and the probability of observing at most that frequency), computed as the inverse of the time gap between releases in months (e.g., one episode every ~30 days ≈ frequency 1). Roughly <strong>80%</strong> of channels publish at high rates (around <strong>18</strong> episodes per month). Daily publishing (26–30 per month) is comparatively rare.</p> 
            <vegachart schema-url="{{site.baseurl}}/assets/charts/frequency_PDF_CDF_chart_leggero.json" style="width: 100%; display: flex; justify-content: center;"></vegachart>

            <br>
            <br>

            <div class="container">
                <div class="header">
                    <button type="button" class="collapsible">Technical analysis</button>
                </div>
                <div class="content">
                    <p>We set out to collect data from 25 YouTube channels, but reduced the final sample to 24 after excluding one channel that did not meet podcast criteria.</p>
                    <p>Episode-level metadata (title, views, description, publication date, likes, duration, and comment count) was collected using <strong>Selenium</strong>, resulting in <strong>13,756</strong> episodes.</p>
                    <p>To collect comment information at scale, we used the <strong>YouTube Data API</strong> (via Google Console tokens) to download first-level comment metadata, including author, text, and timestamp. Comments were stored in a dedicated JSON structure totaling more than <strong>18,000,000</strong> comments.</p>
                    <p>Transcripts were retrieved via YouTube APIs, producing about <strong>13,218</strong> transcript documents. Audio was extracted using a pipeline built with <strong>Pytube</strong>, <strong>Pydub</strong>, <strong>Librosa</strong>, and <strong>FFmpeg</strong>, producing roughly <strong>7,500</strong> audio files for feature extraction. Thumbnails were downloaded using <strong>Requests</strong>, and video frames were captured using <strong>cv2</strong> (OpenCV) and Pytube.</p>
                    <p>The consolidated dataset includes channel metadata (URL, subscribers, channel creation date, total channel views) and episode metadata (views, likes, duration, publication date, comment count). Transcripts were stored separately in CSV files, while comments were stored as JSON for efficient handling at scale.</p>
                </div>
            </div>

            <hr>
        </div>
    </div>
</div>

<div id="topic-extraction" class="anchor-offset" style="text-align: center;">
    <h1 style="color: white; font-size: 48px;">Topic Extraction</h1>
</div>

<div style="position: relative; width: 100%; padding-right: 200px; padding-left: 200px;">
    <div class="row">
        <div class="col-md-3 col-md-offset-3">
        </div>
        <div class="col-md-6">
            <hr>

            <p><strong>Which topics dominate podcast content—and how do they change over time?</strong></p> 

            <p>We extracted themes from episode transcripts and mapped each episode to a primary topic. The topic set includes <em>politics</em>, <em>sports</em>, <em>economy</em>, <em>health</em>, <em>technology</em>, <em>culture</em>, <em>education</em>, <em>environment</em>, <em>crime</em>, <em>entertainment</em>, and <em>music</em>.</p>

            <p>Two clarifications matter. First, <strong>crime</strong> includes not only true-crime storytelling but also war crimes, political crimes, and related reporting. Second, <strong>education</strong> extends beyond school topics to professional development, personal growth, workplace learning, and broader social education themes.</p>

            <p>The chart below shows how topic prevalence evolves across the dataset:</p> 

            <br>
            <vegachart schema-url="{{site.baseurl}}/assets/charts/TOPIC_PROJECT_BLACK_VERO_3.json" style="width: 100%; display: flex; justify-content: center;"></vegachart> 
            <br>

            <p>From 2013 onward, <strong>technology</strong> appears as the most consistent topic in our sample, alongside recurring presence of <strong>crime</strong>, <strong>health</strong>, and <strong>entertainment</strong>. A notable shift is the rise of <strong>politics</strong> beginning in 2017, becoming one of the dominant themes between 2022 and 2024. This trend is amplified by high-output political channels in the dataset, such as MediasTouch and Brian Tyler Cohen.</p>

            <p><strong>Crime</strong> remains a persistent high-appeal theme. Several channels in the dataset are explicitly true-crime focused (e.g., Let’s Read, Law&amp;Crime Network, Bailey Sarian), supporting the idea that some creators lean into crime content because it reliably attracts attention.</p>

            <p>The bubble chart below shows how topics distribute across channels. Clicking on a bubble reveals the main themes discussed by each channel.</p>

            <br>
            <div class="flourish-embed flourish-hierarchy" data-src="visualisation/18816599"><script src="https://public.flourish.studio/resources/embed.js"></script>
            </div>
            <br>

            <div class="container">
                <div class="header">
                    <button type="button" class="collapsible">Technical analysis</button>
                </div>
                <div class="content">
                    <p>This module identifies dominant topics across transcripts using embedding-based classification and a small, interpretable topic dictionary.</p>
                    <p><strong>Preprocessing:</strong> we removed non-semantic annotations (e.g., “[music]”, “[laughing]”) using regular expressions, then tokenized text, removed punctuation and numbers, and lowercased all tokens.</p>
                    <p><strong>Embeddings:</strong> we used the pre-trained <em>GoogleNews-vectors-negative300</em> Word2Vec model (300-dimensional vectors). Each transcript was represented as the mean of its word vectors.</p>
                    <p><strong>Classification:</strong> for each topic, we created a topic vector by averaging embeddings of curated topic keywords. Each transcript was assigned to the topic with the highest cosine similarity between transcript vector and topic vector.</p>
                    <p><strong>Quality check:</strong> a qualitative review of 90 videos found incorrect topic assignment for 25 URLs, indicating useful directional signal but imperfect accuracy.</p>
                </div>
            </div>

            <hr>
        </div>
    </div>
</div>

<div id="sentimenti-analysis" class="anchor-offset" style="text-align: center;">
    <h1 style="color: white; font-size: 48px;">Sentiment analysis</h1>
</div>

<div style="position: relative; width: 100%; padding-right: 200px; padding-left: 200px;">
    <div class="row">
        <div class="col-md-3 col-md-offset-3">
        </div>
        <div class="col-md-6">
            <hr>

            <p>In a platform-native environment like YouTube, podcast success depends not only on reach, but on <strong>audience response</strong>. We analyzed comment sentiment to understand how viewer perception evolves over time.</p>

            <p>Across the years in the dataset, positive comments represent a large share of engagement. However, one pattern stands out: <strong>negative comments increase over time</strong>, suggesting rising polarization, stronger expectations, or more contentious topics.</p>

            <br>
            <br>

            <vegachart schema-url="{{site.baseurl}}/assets/charts/Polarity_Comments 2.json" style="width: 100%; display: flex; justify-content: center;"></vegachart>

            <br>
            <br>

            <p>This trend raises practical questions for creators: what drives the increase in negative feedback, and does the pattern hold across platforms? Negative comments can signal genuine dissatisfaction—but they can also increase visibility by boosting discussion and algorithmic activity.</p>

            <div class="container">
                <div class="header">
                    <button type="button" class="collapsible">Technical analysis</button>
                </div>
                <div class="content">
                    <p>We performed sentiment analysis on YouTube comments using <strong>VADER</strong> (Valence Aware Dictionary and sEntiment Reasoner), a lexicon- and rule-based model optimized for social text.</p>
                    <p>VADER assigns polarity scores using a sentiment lexicon (7,000+ terms, including emoticons) and hand-crafted rules (negations, intensifiers, punctuation patterns) to adjust overall sentiment.</p>
                    <p>We cleaned comment text with two functions: one removed non-alphanumeric characters and accents; the second handled platform-specific elements such as URLs, hashtags, and mentions.</p>
                    <p>Example aggregate VADER output for the dataset:
                    {‘neg’: 0.125, ‘neu’: 0.595, ‘pos’: 0.28, ‘compound’: 0.604}.</p>
                    <p>To improve signal quality, we retained only records with <strong>compound &gt; 0.6</strong>, reducing the working dataset to ~<strong>6 million</strong> comments from ~<strong>18 million</strong>.</p>
                </div>
            </div>

            <hr>
        </div>
    </div>
</div>

<div id="audio" class="anchor-offset" style="text-align: center;">
    <h1 style="color: white; font-size: 48px;">Audio track analysis</h1>
</div>

<div style="position: relative; width: 100%; padding-right: 200px; padding-left: 200px;">
    <div class="row">
        <div class="col-md-3 col-md-offset-3">
        </div>
        <div class="col-md-6">
            <hr>

            <p><strong>How has podcast sound changed over the years?</strong> To answer this, we analyzed audio features from 24 channels across more than <strong>7,500</strong> episodes—roughly <strong>2,765 hours</strong> of processed audio.</p>

            <p>We focused on signal features that capture intensity, timbre, rhythm, and spectral balance: RMS energy (<code>rms_energy</code>), the first Mel-frequency cepstral coefficient (<code>mfcc_1_mean</code>), speech tempo, average pitch (<code>pitch_mean</code>), zero-crossing rate, spectral centroid, and spectral roll-off.</p>

            <br>
            <br>

            <vegachart schema-url="{{site.baseurl}}/assets/charts/chart_audio3.json" style="width: 100%; display: flex; justify-content: center;"></vegachart>

            <br>
            <br>

            <p>One of the clearest signals is a marked change around late 2019: we observe a spike in both expressed energy (<code>rms_energy</code>) and voice timbre intensity (<code>mfcc_1_mean</code>), followed by a decline. A plausible explanation is that creators experimented with higher-energy delivery as the space became more competitive.</p> 

            <p>After 2020, the soundscape shifts: intensity and tempo trend downward, while pitch, zero-crossing rate, and spectral centroid trend upward. The net effect suggests a more relaxed delivery but with greater clarity and definition—potentially optimized for mobile and headphone listening, where intelligibility in noisy environments matters.</p>

            <div class="container">
                <div class="header">
                    <button type="button" class="collapsible">Technical analysis</button>
                </div>
                <div class="content">
                    <p>Audio feature extraction was built on <strong>Librosa</strong> and <strong>Pydub</strong>, optimized for parallel processing on 32 cores using <strong>Dask</strong>.</p>
                    <p>We normalized volume with Pydub for consistent loudness across files, and resampled audio to <strong>44,100 Hz</strong> with Librosa when needed to ensure a uniform sampling rate.</p>
                    <p>Extracted features include zero-crossing rate, RMS energy (mean and standard deviation), signal mean and standard deviation, higher-order statistics (kurtosis, skewness), pitch (mean and std), the first 7 MFCCs, spectral centroid and roll-off (mean and std), and tempo. Results were stored in CSV and merged with episode metadata.</p>
                    <p>For visualization, we removed outliers, applied monthly aggregation, standardized features, and used moving averages. The interactive time-series visualization was produced with <strong>Altair</strong>.</p>
                </div>
            </div>

            <hr>
        </div>
    </div>
</div>

<div id="frame-color" class="anchor-offset" style="text-align: center;">
    <h1 style="color: white; font-size: 48px;">Frame color analysis</h1>
</div>

<div style="position: relative; width: 100%; padding-right: 200px; padding-left: 200px;">
    <div class="row">
        <div class="col-md-3 col-md-offset-3">
        </div>
        <div class="col-md-6">
            <hr>
            <br>

            <div style="text-align: center;">
                <h2 style="color: white; font-size: 28px;">Frame</h2>
            </div>

            <br>

            <p>Podcasters often treat on-camera color choices as secondary. Viewers, too, frequently assume that color has little impact on engagement—especially in a format that is perceived as “audio-first.”</p>

            <p>Our analysis suggests the opposite. Color composition is a meaningful variable: it shapes perceived comfort, guides attention, and helps maintain viewer retention during episodes that can last hours.</p>

            <p>To quantify this effect, we extracted representative frames across all podcasts and tracked the dominant scene colors over the widest time span possible, to capture changes driven by production trends and audience expectations.</p>

            <p>The animation below shows how dominant scene colors evolved over time.</p>

            <br>
            <br>

            <div class="flourish-embed flourish-bar-chart-race" data-src="visualisation/18803566"><script src="https://public.flourish.studio/resources/embed.js"></script></div>

            <br>
            <br>
            <br>

            <p><strong>Important note:</strong> the colors displayed are computed <em>independently</em> of lighting differences. We extracted HSL values from frames and removed saturation and lightness, keeping only <strong>Hue</strong>. If we had kept exposure, the result would largely collapse into a grayscale ranking—because most sets are intentionally lit to feel “warm and inviting.” Removing exposure isolates the actual color choices in props, backgrounds, and set design.</p>

            <p>With this adjustment, the trend is clear: the dataset shifts over time from cooler palettes toward <strong>warmer</strong> ones. Warm hues are associated with comfort, human closeness, and familiarity—qualities that matter in long-form conversational video. Exceptions exist (stylistic identity, topic context, intentional differentiation), but the overall drift is toward warm tones.</p>

            <br>
            <br>

            <div style="text-align: center;">
                <h2 style="color: white; font-size: 28px;">Thumbnails</h2>
            </div>

            <br>

            <p>We repeated the same analysis on thumbnails—the cover images shown on YouTube’s homepage, search results, and recommendations. Thumbnails are a high-leverage decision point: they often determine whether a user clicks at all.</p>

            <br>
            <br>

            <div class="flourish-embed flourish-bar-chart-race" data-src="visualisation/18803719"><script src="https://public.flourish.studio/resources/embed.js"></script></div>

            <br>
            <br>

            <p>Thumbnail results closely mirror frame results, but with fewer exceptions. Thumbnails are more tightly optimized for attention: warm, high-impact colors dominate because they push urgency, energy, and emotional salience during the “click decision.”</p>

            <p>In practice, thumbnails also tend to employ mild click-optimization—amplifying curiosity and anticipation beyond what the episode may fully deliver. It is not accidental that many attention signals in the real world (warnings, hazards, alerts) use red, orange, and yellow—colors that also dominate the thumbnail trends observed here.</p>

            <div class="container">
                <div class="header">
                    <button type="button" class="collapsible">Technical analysis</button>
                </div>
                <div class="content">
                    <p>Frame color analysis required a pipeline from frame extraction through color clustering and time-based aggregation.</p>

                    <p><strong>Frame extraction</strong></p>
                    <p>We used <strong>Pytube</strong> to download videos and <strong>OpenCV (cv2)</strong> for image processing. Because the goal was to capture all colors used on set, we detected shot changes and saved a representative frame per shot.</p>
                    <p>Each video frame was converted to grayscale and a histogram of gray levels was computed. Consecutive-frame histograms were compared using correlation. When correlation dropped below a threshold, we flagged a scene change and saved the corresponding frame.</p>
                    <p>To avoid double counting repeated shots, we computed perceptual hashes (via <code>imagehash.phash</code>) for candidate frames and kept only frames with sufficiently distinct hashes. Downloaded videos were deleted after processing to preserve disk space.</p>

                    <p><strong>Color extraction</strong></p>
                    <p>We resized frames for efficiency, converted them to numpy arrays, aggregated pixels, and applied <strong>K-means</strong> clustering (scikit-learn) to identify dominant colors. For each dominant color, we computed RGB as well as HSV, HSL, and Luma measures. HSL was used to isolate Hue and remove exposure effects.</p>

                    <p><strong>Color analysis</strong></p>
                    <p>We built a dataframe linking each video to its dominant Hue and publication date. Since many colors initially clustered around grayscale (due to lighting), we removed saturation and lightness and used only Hue. Hue values were mapped back to RGB for visualization, then clustered into <strong>10</strong> macro color categories via K-means to avoid over-fragmentation. The time evolution was visualized using a dynamic bar chart.</p>

                    <p>The thumbnail pipeline used the same methodology.</p>
                </div>
            </div>

            <hr>
        </div>
    </div>
</div>

<div id="conclusioni" class="anchor-offset" style="text-align: center;">
    <h1 style="color: white; font-size: 48px;">Conclusions</h1>
</div>

<div style="position: relative; width: 100%; padding-right: 200px; padding-left: 200px;">
    <div class="row">
        <div class="col-md-3 col-md-offset-3">
        </div>
        <div class="col-md-6">
            <hr>

            <p><strong>What influences a podcast’s views, likes, and comments on YouTube?</strong></p>
            <p>Our modeling highlights different drivers for each engagement metric—audio, visuals, and channel attributes do not affect views, likes, and comments in the same way.</p>

            <br>

            <h4 style="text-align: center;">Podcast Views</h4>

            <p>On the audio side, <strong>lower pitch</strong> (deeper voices) is associated with higher views. Specific timbre features also matter: MFCC coefficients <strong>1, 6, and 7</strong> correlate positively with views, while MFCC <strong>4 and 5</strong> correlate negatively.</p>

            <p>Visually, <strong>more vivid and saturated colors</strong> generally attract more views. Interestingly, <strong>darker tones</strong> also correlate with higher views—suggesting that “cinematic” or high-contrast aesthetics may perform well even when less bright.</p>

            <p>Channel and structural variables behave as expected: <strong>longer videos</strong> tend to accumulate more views, channels with more <strong>subscribers</strong> have greater visibility, and <strong>older videos</strong> have higher views simply due to longer time on platform.</p>

            <br>

            <vegachart schema-url="{{site.baseurl}}/assets/charts/regression_views_3.json" style="width: 100%; display: flex; justify-content: center;"></vegachart>

            <br>

            <h4 style="text-align: center;">Podcast Likes</h4>

            <p>Likes align with some view drivers but differ in key ways. Lower pitch still correlates with more likes, and MFCC features (notably <strong>1 and 5</strong>) play a role. We also observe a positive relationship between high-frequency energy (clearer, brighter audio) and likes—consistent with preference for intelligible sound.</p>

            <p>Unlike views, likes are more sensitive to <strong>thumbnail aesthetics</strong>: more saturated and brighter thumbnails correlate with more likes. For frames, the relevant signal shifts from intensity/brightness to <strong>Hue</strong>: higher frame hue values are associated with more likes.</p>

            <p>Another divergence: <strong>longer videos correlate negatively with likes</strong>. Finally, videos with <strong>more people in the thumbnail</strong> tend to receive more likes.</p>

            <br>

            <vegachart schema-url="{{site.baseurl}}/assets/charts/regression_likes_3.json" style="width: 100%; display: flex; justify-content: center;"></vegachart>

            <br>

            <h4 style="text-align: center;">Podcast Comments</h4>

            <p>Comment volume correlates with a more activation-driven profile. Faster speech tempo and MFCC <strong>1 and 5</strong> correlate with more comments, while MFCC <strong>4 and 7</strong> correlate negatively.</p>

            <p>On the visual side, <strong>higher hue values</strong> and <strong>more intense colors</strong> are associated with more comments; brightness shows weaker influence. Bright and vivid thumbnails also correlate with comment growth.</p>

            <p>In contrast to views, <strong>older and longer videos tend to receive fewer comments</strong>, likely reflecting declining conversation over time. As with likes, <strong>more people in the thumbnail</strong> is associated with more comments.</p>

            <br>

            <vegachart schema-url="{{site.baseurl}}/assets/charts/regression_comments_3.json" style="width: 100%; display: flex; justify-content: center;"></vegachart>           

            <br>

            <div class="container">
                <div class="header">
                    <button type="button" class="collapsible">Technical analysis</button>
                </div>
                <div class="content">
                    <p>We modeled three dependent variables—<strong>views</strong>, <strong>likes</strong>, and <strong>comments</strong>—against a panel of regressors spanning audio features, image features, and channel-level attributes.</p>
                    <p>The original dataset included multiple color representations (RGB, HSL, HSV, Luma) and the count of detected people in the thumbnail.</p>
                    <p>We removed records without publication dates, which are required to compute the “days since publication” variable.</p>
                    <p>Audio coverage was smaller than video coverage due to extraction constraints, reducing the number of usable records. We considered rebalancing methods (under/over-sampling, SMOTE) but avoided synthetic data to preserve interpretability and minimize artifacts.</p>
                    <p>Audio features were standardized (z-scored) to produce directly comparable coefficient magnitudes.</p>
                    <p>Correlation analysis showed strong collinearity among RGB features; HSL provided lower correlation and better interpretability. We removed highly correlated predictors, including: <code>standardized_mfcc_3</code>, <code>standardized_spectral_rolloff</code>, <code>standardized_rms_energy</code>, and <code>Total_Videos</code>.</p>
                    <p>The final correlation matrix shows a maximum correlation of <strong>+0.64</strong> (between <code>standardized_mfcc_2</code> and <code>standardized_spectral_centroid</code>) and a minimum of <strong>-0.44</strong> (between <code>standardized_mfcc_1</code> and <code>audio_kurtosis</code>).</p>
                    <p>Outlier detection was initially tested on all variables, but we applied it primarily to dependent variables to avoid excessive record loss.</p>
                    <p>For count outcomes, we first considered Poisson regression but rejected it due to overdispersion (variance &gt; mean). We therefore used <strong>Negative Binomial</strong> regression and estimated coefficients with a robust covariance specification.</p>
                    <p>Because the model uses a log link, coefficients are interpreted via exponentiation. We report effects as <code>exp(beta) - 1</code>, which maps results to intuitive percent increases/decreases.</p>
                    <p>A key limitation is dataset breadth: reduced audio coverage (~40% relative to video coverage) may constrain statistical power for audio-related findings.</p>
                </div>
            </div>

        </div>
    </div>
</div>

<!--
<div class="row pb-5">
    <div class="col-md-12 col-sm-12">
        <div class="card-container">
            {% for image in site.data.home-cards %}
            <div class="card" style="width: 18rem;">
                    <a href="{{site.baseurl}}{{ image.path}}">
                    <div class="card-img"  ><img src="{{site.baseurl}}{{ image.url}}" class="card-img-top" alt="{{ image.name }}">
                    </div>
                    <div class="card-body">
                        <h5 class="card-title">{{ image.name }}</h5>
                        <p class="card-text">{{ image.description }}</p>
                    </div>
                    </a>    
            </div>
            {% endfor %}
        </div>
    </div>
</div>

<div class="container py-3 mb-0 bg-color-full bg-color">
    <div class="row">
        <div class="col-md-3 col-md-offset-3">
        </div>
        <div class="col-md-6">
            <p>Before building the site, you need to install Jekyll</p>
            <a href="{{site.baseurl}}/installation" class="btn btn-info" role="button">Jekyll Installation</a>
        </div>
    </div>
</div>
-->
