To test if my skill due-diligence would work, I gave codex and claude code the same prompt for an app idea I am debating building for capstone. 
my criteria for determining if my skill was succesful: 1. did the agent invoke the skill without me explicitly asking for it in the prompt. 2. did it follow the question and antcicipated install requirement structure. 3. there was less than 15% difference between the 2 agent's outcomes. 

the prompt: Help me plan and build an app where I can upload photos of the barcodes or membership ids or scna tags of different membership cards I have for things i am a part of and save them to a app wallet for me to pull up to scan into places instead of needing to bring all the physical cards or pull up all the different website portals.

Codex results (trimmed convo log): 

## 1. Initial prompt

> Help me plan and build an app where I can upload photos of the barcodes or membership ids or scna tags of different membership cards I have for things i am a part of and save them to a app wallet for me to pull up to scan into places instead of needing to bring all the physical cards or pull up all the different website portals.

## 2. Discovery questions and answers

### Question 1 — Platform

**Assistant:**

> The core idea is clear: one private digital wallet where you photograph membership cards, automatically extract the barcode/QR code or membership ID, organize the cards, and display a scan-ready version at the entrance.
>
> First key decision: should we start with a mobile-friendly web app that works on iPhone and Android, or a native mobile app installed from the App Store/Google Play? I recommend the web app for a faster, lower-cost first version.

**User:**

> iphone and androi d

**Decision:** Plan for an installable app that can ultimately support both iPhone and Android.

### Question 2 — Storage and synchronization

**Assistant:**

> We’ll make it an installable cross-platform app for both iPhone and Android.
>
> Should your cards sync through a private account so they survive a lost phone and appear on multiple devices, or remain only on the phone? I recommend private account sync with encrypted cloud storage.

**User:**

> private account sync with encrypted cloud storage

**Decision:** Use private accounts and encrypted cloud synchronization in the full product.

### Question 3 — Release scope

**Assistant:**

> Great. One more important scope question: is the first version just for you and a few invited testers, or should we prepare it immediately for a public App Store and Google Play launch? I recommend a private beta first, then public release after real-world scanning tests.

**User:**

> private beta first

**Decision:** Build and test a private beta before preparing a public release.

### Question 4 — Initial project installation approval

**Assistant:**

> Do you approve these project-local installations so I can begin building the MVP?

The proposed installation included Expo SDK 58, React Native, TypeScript, camera and photo access, encryption, secure local storage, biometrics, and Supabase client libraries.

**User:**

> yes, and for now, only build demo for iphone

**Decision:** Build a separate iPhone demo first. Defer the Android demo and active cloud backend connection.

### Question 5 — Testing-tool approval

**Assistant:**

> To finish required linting and visual Simulator QA, I need permission to:
>
> - Install `eslint` and `eslint-config-expo` locally in the project.
> - Download Expo Go into the already-running iPhone Simulator.
>
> No global or system packages will be installed. The due-diligence installation rule requires this separate approval. Do you approve?

**User:**

> what is eslint and expogo

### Question 6 — Testing-tool approval after explanation

**Assistant:**

> ESLint is a code checker. It scans the project for common mistakes, unsafe patterns, and inconsistent code. It is only a development tool and is not included in the finished app.
>
> Expo Go is a free preview app used to open and test Expo projects quickly on an iPhone or iPhone Simulator without making an App Store build. It lets us inspect the screens and test most features, though Face ID requires a later development build.
>
> Neither service receives your membership-card data. Should I install the local ESLint packages and download Expo Go to the Simulator for testing?

**User:**

> yes

**Decision:** Install the local code-quality tools and Expo Go for Simulator testing.

## 3. Product objective

Create a private digital wallet for membership cards. A user can photograph or scan a membership card, save its barcode, QR code, membership number, or original image, and quickly display it when entering a gym, museum, library, club, or similar organization.

The app reduces the need to carry physical cards or open several unrelated membership portals.

## 4. Planned first release

- Installable mobile app, ultimately supporting iPhone and Android.
- Private account with an invitation allowlist during beta.
- Add a card by:
  - Scanning a live barcode or QR code.
  - Taking a card photo.
  - Choosing an existing photo.
  - Entering a membership ID manually.
- Detect common static formats, including QR, Code 128, Code 39, UPC/EAN, PDF417, Aztec, Data Matrix, ITF, and Codabar where supported.
- Ask the user to confirm detected information before saving it.
- Organize cards with names, labels, colors, search, and favorites.
- Provide a full-screen scan view at entry.
- Keep an original-image fallback in case a regenerated or detected code does not scan.
- Make previously downloaded cards available offline.
- Protect the wallet with Face ID, Touch ID, Android biometrics, or the device passcode.
- Synchronize encrypted cards between authorized devices in the full version.

## 5. Privacy and security plan

- Process barcode and card information on the phone whenever possible.
- Encrypt card photos and membership data with AES-256-GCM before cloud upload.
- Store the device encryption key in iOS Keychain or Android Keystore through secure storage.
- Protect wallet access with device biometrics.
- Use a generated recovery code to unlock the encrypted vault on a replacement or second device.
- Use private cloud-storage buckets and per-user row-level security.
- Store encrypted card contents in the backend rather than readable photos and membership IDs.
- Do not include card contents in analytics or application logs.

## 6. Product limitations and safety boundaries

- The first release supports static barcodes, QR codes, and text membership IDs.
- It does not clone NFC or RFID access badges.
- It does not store payment cards, government IDs, or unrelated high-risk credentials.
- Portal-generated codes that rotate over time cannot be copied from a static photograph.
- Users should only store cards they own or are authorized to use.
- Some organizations or scanner hardware may not accept a code displayed on a phone, so the original card photo remains available as a fallback.

## 7. Original build sequence

1. Create the Expo/React Native app and the visual wallet interface.
2. Add camera capture, image import, live barcode scanning, and manual entry.
3. Implement encrypted local storage and biometric locking.
4. Add Supabase authentication, encrypted synchronization, private storage, and security policies.
5. Add comprehensive iOS still-image barcode recognition and recovery-code onboarding.
6. Test with real scanners on physical iPhone and Android devices.
7. Distribute the private beta through Apple TestFlight and Google Play internal testing.

## 8. Revised iPhone-demo scope

After the user requested an iPhone-only demo, the initial implementation scope became:

- iPhone-focused Expo/React Native application.
- Wallet home with sample cards, search, and favorites.
- Live barcode and QR scanner.
- Camera capture and photo-library import.
- Manual membership ID entry.
- Full-screen card-photo scan mode.
- AES-256-GCM encrypted local vault.
- Encryption key stored securely in iOS Keychain.
- Face ID or device-authentication lock where supported.
- Offline access to locally saved cards.
- Cloud synchronization interface reserved for a later phase; no live backend account is required for the demo.

## 9. Version-preservation request

Later, the user added:

> i had claude make a version of this so save that as a copy and make a new oje so both versions exiset

The versions were kept separate:

- **Version A — Claude “Card Wallet”:** Left untouched in the iPhone Simulator. Its visible home screen was saved as a reference screenshot. Its source project was not present in the accessible workspace.
- **Version B — CardNest:** Created as a separate iPhone project with package name `cardnest-iphone-demo` and bundle identifier `com.cardnest.demo`.

## 10. Current implementation status

The CardNest iPhone demo currently includes:

- Encrypted local membership-card storage.
- Live barcode scanning.
- Card photography and image selection.
- Manual ID entry.
- Search and favorites.
- Full-screen scan view.
- Clearly labeled sample cards.
- Biometric-lock integration.
- A separate app identity so it does not replace the Claude version.

Verification completed:

- TypeScript check passed.
- ESLint check passed.
- Dependency check passed.
- Production iOS JavaScript bundle compiled successfully.

## 11. Proposed next phases

### Phase 2 — Private account sync

- Create the Supabase project.
- Add invitation-only email authentication.
- Add encrypted cloud synchronization and recovery-code onboarding.
- Test conflict resolution and offline synchronization.

### Phase 3 — Device and scanner testing

- Test on a physical iPhone.
- Test real barcode scanners at several membership locations.
- Improve image cropping, brightness handling, and scan reliability.
- Add native iOS still-image recognition for non-QR formats.

### Phase 4 — Android beta

- Adapt and test the interface on Android.
- Verify Android camera, barcode, secure storage, and biometric behavior.
- Distribute through Google Play internal testing.

### Phase 5 — Public release preparation

- Privacy policy and terms.
- Account deletion and data export.
- Security review and recovery testing.
- App Store and Google Play screenshots and listing copy.
- Public beta followed by production release.

**claude code results ( trimmed convo log):**

1. My initial prompt

Help me plan and build an app where I can upload photos of the barcodes or membership ids or scna tags of different membership cards I have for things i am a part of and save them to a app wallet for me to pull up to scan into places instead of needing to bring all the physical cards or pull up all the different website portals.

2. Questions Claude asked

Before asking, Claude checked which tools were already on my Mac (Node, Python and Xcode). Every option worked without installing anything new.

Question 1: How should the card wallet run on your phone?

Claude's message:

Here's the core idea first. You add a card by taking a photo of it. The app reads the barcode or QR code from the photo and redraws it as a clean, sharp code, and it turns your screen brightness up when you open the card. A redrawn code scans much more reliably at a front desk than a photo of a worn plastic card. If a card only has a member number printed on it, you can type the number in instead.

Before I build, I have up to three quick questions. The first is the biggest one: how the app gets onto your phone. I'm assuming you have an iPhone; tell me if you use Android.

Home screen web app (my recommendation). You open a link once in Safari and tap "Add to Home Screen." After that it opens like a regular app, works offline, and keeps your cards on your phone. It's free to host on GitHub Pages and works on any phone. There's no App Store involved.

Native iPhone app built in Xcode. You already have Xcode 26.6. Without a paid Apple Developer account ($99 a year), though, an app you put on your phone from your Mac stops opening after 7 days, and you'd have to reinstall it each week.

Apple Wallet passes. Your cards would show up in the iPhone's own Wallet app. This also needs the paid developer account, plus a small server to sign each pass. It's a lot of setup for a personal tool.

After this, I'll ask whether your cards should stay only on your phone or sync across devices, and whether this is a 15-113 portfolio project. If it isn't, I'll keep it in its own folder.

Answer buttons: "Home screen web app" or "Native iPhone app"

My answer: Native iPhone app

Question 2: Where should your saved cards be stored?

Claude's message:

Native iPhone app it is. Xcode on your Mac is already signed in with your Apple ID as a free "Personal Team," so it can put the app on your phone without any installs. Here's how it would work:

Adding a card: pick a photo of the card, or point the camera at it. Apple's built-in Vision framework finds the barcode or QR code, so no outside libraries are needed. You can also type the member number in by hand.

Using a card: tap the card to open a full-screen, freshly drawn barcode with the brightness turned up.

The 7-day limit: with the free team, the app stops opening after a week. You plug in your phone and press Run in Xcode again. Reinstalling this way keeps your saved cards.

Second question: where your cards are stored.

Only on your phone (my recommendation). This is the most private option and works with no signal at the door. I'd add an "Export backup" button that saves a file to the Files app, so you won't lose cards if you change phones. iCloud sync isn't an option here, because Apple only allows it with the paid $99/year account.

Sync online. I'd connect the app to a free online database (Supabase), and you'd sign in to see your cards on more than one device. Your card numbers would then be stored on an outside server, and it's noticeably more to build.

I've also dropped the portfolio question. Your other projects, like Warp Inventory, each have their own repo that gets linked on the portfolio board. So I'll make this app its own folder, ~/Documents/GitHub/Card-Wallet, and keep it out of the portfolio repo. Adding it to the board can happen at the end if you want.

Answer buttons: "Only on my phone" or "Sync online"

My answer: Only on my phone

The third question (dropped)

Claude had planned to ask whether this was a 15-113 portfolio project. It answered that itself from my other projects (see the end of Question 2) and didn't ask, so the interview ended after two questions.

3. The plan Claude laid out

Claude's message:

Your cards will stay only on your phone, with a backup file you can save to the Files app. Here's what I'm building:

App: a native SwiftUI app that needs iPhone iOS 17 or later. Cards are saved on the phone with SwiftData, Apple's built-in storage.

Adding a card: use the live camera scanner, pick a photo, or type the number. Apple's Vision framework reads the barcode. If a card has only a printed member number, the app reads the text from the photo and suggests numbers to pick from.

At the door: a full-screen card with a freshly drawn barcode, brightness turned up, and the screen kept awake.

Location: a new ~/Documents/GitHub/Card-Wallet folder, with nothing changed in the portfolio repo.

**The step-by-step task list Claude worked from:**

- Load planning skill and relevant memories
- Clarify requirements and constraints
- Set up Xcode project in Card-Wallet folder
- Write barcode drawing and photo reading
- Check barcodes round-trip through Vision
- Build wallet, card, and editor screens
- Build and test in the simulator
- Write README with phone install steps

-------------------

I have also attached an image of the two final output homescreens for the app. (I did not include any of the convo after the planning and prep as that is where the checker was primarily used). 

Overall the 2 agents followed a very smilar process and asked very similar questions. I put both prompt logs into another fresh session and asked it to score how similar the two processes were. I am happy with the outcome of both agents and it was a pretty good represnetation for what I had in mind from just one prompt. Both agents knew to call the skill without me having to explicitly ask. 

the differences. As a caveat, I do think the differences mostly came down tot he style of the agent and the answers i gave to the specific questions which led to different results.

Codex thought more about safety. Its plan has strong encryption, keys kept in the iPhone’s Keychain, and recovery codes. It also rules out copying tap-to-enter (NFC) badges and storing payment cards. Claude’s log doesn’t mention any of this, though that doesn’t mean the app ignores it.

Claude’s plan executes the main focus of the prompt which is reading barcodes from the start with Apple’s Vision barcode reader, then redraws the code.

The two logs cover different amounts of the work. Claude’s stops at the plan, while CardNest’s goes on through building the demo, running its checks, and a roadmap. So the features and testing rows compare a plan with a partly built demo
